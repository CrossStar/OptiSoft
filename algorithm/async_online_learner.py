# 文件：async_online_learner.py
import aiomysql
from river import (
    metrics,
    multioutput,
    stream,
    preprocessing,
    neighbors,
    imblearn,
    forest,
)
import pandas as pd
import asyncio

from settings import *
import os


class AsyncOnlineLearning:
    def __init__(self, base_model: str = "ARF"):
        # 读取环境变量
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        db = os.getenv("DB_NAME")

        self.db_config = dict(
            host=host,
            user=user,
            password=password,
            db=db,
            autocommit=True,
        )
        self.table = "motor_result_mmid"
        self.last_seen_id = 0
        self.base_model = base_model

        if self.base_model == "KNN":
            # 使用 KNN 模型
            base_model_instance = imblearn.HardSamplingRegressor(
            regressor=neighbors.KNNRegressor(),
            p=0.2,
            size=30,
            seed=42,
            )
            self.model = multioutput.RegressorChain(
            model=preprocessing.StandardScaler() | base_model_instance,
            order=["AvgTorque", "TorqueRipple"],
            )
        elif self.base_model == "ARF":
            # 使用 ARF 模型
            base_model_instance = forest.ARFRegressor()
            self.model = multioutput.RegressorChain(
            model=preprocessing.StandardScaler() | base_model_instance,
            order=["AvgTorque", "TorqueRipple"],
            )
        else:
            raise ValueError(f"Unsupported base_model: {self.base_model}")

        self.mae_metrics = {"AvgTorque": metrics.MAE(), "TorqueRipple": metrics.MAE()}

        self.results = {
            "id": [],
            "true_avg": [],
            "pred_avg": [],
            "mae_avg": [],
            "true_ripple": [],
            "pred_ripple": [],
            "mae_ripple": [],
        }

    async def connect(self):
        self.pool = await aiomysql.create_pool(**self.db_config)
        print("数据库连接已建立")

    @async_timeit
    async def initial_train(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(f"SELECT * FROM {self.table} ORDER BY id ASC")
                all_rows = await cursor.fetchall()
                df = pd.DataFrame(all_rows)
                await self._learn_from_dataframe(df)

    async def _learn_from_dataframe(self, df):
        if df.empty:
            return

        self.last_seen_id = df["id"].max()

        y = df[["AvgTorque", "TorqueRipple"]]
        X = df.drop(columns=["id", "Status", "Timestamp", "AvgTorque", "TorqueRipple"])

        # 保留 ID 列用于记录
        ids = df["id"].tolist()

        for idx, (xi, yi) in enumerate(stream.iter_pandas(X, y)):
            y_pred = self.model.predict_one(xi)
            self.model.learn_one(xi, yi)

            if y_pred != {}:
                # pred_avg = y_pred.get("AvgTorque", 0.0)
                # pred_ripple = y_pred.get("TorqueRipple", 0.0)
                pred_avg = y_pred["AvgTorque"]
                pred_ripple = y_pred["TorqueRipple"]

                self.mae_metrics["AvgTorque"].update(yi["AvgTorque"], pred_avg)
                self.mae_metrics["TorqueRipple"].update(yi["TorqueRipple"], pred_ripple)

                self.results["id"].append(ids[idx])  # 正确记录该条数据的 ID
                self.results["true_avg"].append(yi["AvgTorque"])
                self.results["pred_avg"].append(pred_avg)
                self.results["mae_avg"].append(self.mae_metrics["AvgTorque"].get())

                self.results["true_ripple"].append(yi["TorqueRipple"])
                self.results["pred_ripple"].append(pred_ripple)
                self.results["mae_ripple"].append(
                    self.mae_metrics["TorqueRipple"].get()
                )

    async def poll_and_learn(self, interval=3):
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                while True:
                    await cursor.execute(
                        f"SELECT * FROM {self.table} WHERE id > {self.last_seen_id} ORDER BY id ASC"
                    )
                    new_rows = await cursor.fetchall()
                    df_new = pd.DataFrame(new_rows)
                    await self._learn_from_dataframe(df_new)

                    if not df_new.empty:
                        print(
                            f"[+{len(df_new)}] 已学习新数据，最新 ID: {self.last_seen_id}"
                        )

                    await asyncio.sleep(interval)

    async def close(self):
        self.pool.close()
        await self.pool.wait_closed()
        print("数据库连接池已关闭")
