from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from async_online_learner import AsyncOnlineLearning
import asyncio
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from optimizer import surrogate_model_optimizer
import numpy as np

model = AsyncOnlineLearning(base_model="KNN")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 初始化模型
    await model.connect()
    await model.initial_train()
    # 启动学习任务
    task = asyncio.create_task(model.poll_and_learn(interval=3))
    try:
        yield
    finally:
        task.cancel()  # 在关闭时取消任务
        await model.close()

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/results")
async def get_results():
    return model.results

@app.get("/api/optimize_results")
async def get_optimize_results():
    F = np.load("results/last_F.npy")
    pareto_front = [[float(f[0]), float(f[1])] for f in F]
    return {"pareto_front": pareto_front}

@app.post("/api/start_optimization")
async def start_optimization(n_gen: int = 300, n_pop: int = 150):
    result = await surrogate_model_optimizer(model, n_gen=n_gen, n_pop=n_pop)

    # 保存结果到文件或内存
    np.save("results/last_X.npy", result["X"])
    np.save("results/last_F.npy", result["F"])
    return {"message": "Optimization completed.", "feature_names": result["feature_names"], "X": result["X"].tolist(), "F": result["F"].tolist()}

@app.get("/avgTorque")
async def avg_page():
    return FileResponse("static/avgTorque.html")

@app.get("/rippleTorque")
async def ripple_page():
    return FileResponse("static/rippleTorque.html")

@app.get("/pareto_front")
async def pareto_front():
    return FileResponse("static/pareto_front.html")


import sys
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5632)