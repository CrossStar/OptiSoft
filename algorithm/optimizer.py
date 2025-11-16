import numpy as np
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.optimize import minimize

from settings import *

class SurrogateProblem(Problem):
    def __init__(self, surrogate_model):
        super().__init__(n_var=4, n_obj=2, n_ieq_constr=1,
                         xl=np.array([1.0, 2.0, 0.5, 14.0]),
                         xu=np.array([4.0, 5.0, 1.5, 17.0]))
        self.model = surrogate_model.model
        self.Din, self.depth = 58.0, 12.0
        self.constraint_target = self.constraint_expression(2.5, 3.5, 1.0)
        self.feature_names = ["SlotOpen", "ToothWidth", "ToothTipDepth", "MagAngle"]

    def constraint_expression(self, SlotOpen, ToothWidth, ToothTipDepth):
        ToothTipAngle = np.deg2rad(18.55)
        m2mm = 1000.0

        outer_radius = (self.Din / 2 + self.depth + ToothTipDepth) / m2mm
        inner_radius = (
            self.Din / 2
            + (np.pi * self.Din / 18 - SlotOpen - ToothWidth) * np.tan(ToothTipAngle)
            / 2
        ) / m2mm
        tooth_area = ToothWidth * self.depth / (m2mm**2)

        term1 = np.pi * outer_radius**2
        term2 = np.pi * inner_radius**2
        term3 = 18 * tooth_area

        return term1 - term2 - term3

    def _evaluate(self, X, out, *args, **kwargs):
        F = []
        expr_list = []
        for xi in X:
            SlotOpen, ToothWidth, ToothTipDepth, _ = xi

            features = dict(zip(self.feature_names, xi))
            prediction = self.model.predict_one(features)
            avg_torque = -prediction["AvgTorque"]
            torque_ripple = prediction["TorqueRipple"]

            F.append([avg_torque, torque_ripple])

            expr = self.constraint_expression(SlotOpen, ToothWidth, ToothTipDepth)
            expr_list.append(expr)

        F = np.array(F)
        expr_list = np.array(expr_list)
        out["F"] = F
        out["G"] = (
            np.abs(expr_list - self.constraint_target) / self.constraint_target - 5e-2
        ).reshape(-1, 1)


@async_timeit
async def surrogate_model_optimizer(model, n_gen=10, n_pop=100):
    ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=12)
    algorithm = NSGA3(pop_size=n_pop, ref_dirs=ref_dirs)
    problem = SurrogateProblem(model)

    res = minimize(
        problem,
        algorithm,
        termination=('n_gen', n_gen),
        seed=42,
        verbose=False,
    )

    return {
        "feature_names": problem.feature_names,
        "X": res.X,
        "F": res.F,
    }


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from pymoo.core.problem import Problem
# from pymoo.algorithms.soo.nonconvex.ga import GA
# from pymoo.optimize import minimize
# from pymoo.core.callback import Callback

# class SurrogateProblem(Problem):
#     def __init__(self, surrogate_model):
#         super().__init__(
#             n_var=4,
#             n_obj=1,
#             n_ieq_constr=1,
#             xl=np.array([1.0, 2.0, 0.5, 14.0]),
#             xu=np.array([4.0, 5.0, 1.5, 17.0]),
#         )
#         self.model = surrogate_model.model
#         self.Din, self.depth = 58.0, 12.0
#         self.constraint_target = self.constraint_expression(2.5, 3.5, 1.0, np.deg2rad(17.0))
#         self.feature_names = ["SlotOpen", "ToothWidth", "ToothTipDepth", "MagAngle"]

#     def constraint_expression(self, SlotOpen, ToothWidth, ToothTipDepth, MagAngle_rad):
#         term1 = np.pi * (self.Din / 2 + self.depth + ToothTipDepth) ** 2
#         inner = (np.pi * self.Din / 18 - SlotOpen - ToothWidth) / (2 * np.tan(MagAngle_rad))
#         term2 = np.pi * (self.Din / 2 + inner) ** 2
#         term3 = 18 * (ToothWidth * self.depth)
#         return 100 * (term1 - term2 - term3)

#     def _evaluate(self, X, out, *args, **kwargs):
#         F = []
#         expr_list = []
#         for xi in X:
#             SlotOpen, ToothWidth, ToothTipDepth, MagAngle_deg = xi
#             MagAngle_rad = np.deg2rad(MagAngle_deg)

#             features = dict(zip(self.feature_names, xi))
#             prediction = self.model.predict_one(features)
#             avg_torque = -prediction["AvgTorque"]

#             F.append([avg_torque])

#             expr = self.constraint_expression(SlotOpen, ToothWidth, ToothTipDepth, MagAngle_rad)
#             expr_list.append(expr)

#         F = np.array(F)
#         expr_list = np.array(expr_list)
#         out["F"] = F
#         out["G"] = (np.abs(expr_list - self.constraint_target) - 1e-2).reshape(-1, 1)

# class MyCallback(Callback):
#     def __init__(self):
#         super().__init__()
#         self.best_f = []

#     def notify(self, algorithm):
#         # 记录当前代的最优值（最小化问题）
#         current_best = np.min(algorithm.pop.get("F"))
#         self.best_f.append(current_best)

# async def surrogate_model_optimizer(model, n_gen=10, n_pop=100):
#     algorithm = GA(pop_size=n_pop)
#     callback = MyCallback()

#     res = minimize(
#         SurrogateProblem(model),
#         algorithm,
#         termination=("n_gen", n_gen),
#         seed=42,
#         verbose=True,
#         callback=callback,
#     )

#     # 检查 res.X 是否是一维，如果是一维，转为二维
#     X_result = res.X
#     if X_result.ndim == 1:
#         X_result = np.expand_dims(X_result, axis=0)

#     df = pd.DataFrame(X_result, columns=["SlotOpen", "ToothWidth", "ToothTipDepth", "MagAngle"])
#     df["AvgTorque"] = -res.F.reshape(-1)
#     df.to_csv("optimization_results.csv", index=False)

#     # 绘制适应度随迭代次数的变化曲线
#     generations = np.arange(1, len(callback.best_f) + 1)
#     best_fitness = [-f for f in callback.best_f]  # 取正值表示 AvgTorque

#     plt.plot(generations, best_fitness, 'bo-', label="Best AvgTorque per Generation")
#     plt.title("Fitness over Generations")
#     plt.xlabel("Generation")
#     plt.ylabel("Best AvgTorque")
#     plt.legend()
#     plt.grid(True)
#     plt.savefig("fitness_over_generations.png")
#     plt.show()
