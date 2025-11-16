import sys
import json
from ansys.aedt.core import Maxwell2d
from ansys.aedt.core.aedt_logger import AedtLogger

logger = AedtLogger()

def run_optimization(project_file):
    try:
        logger.info("启动优化任务...")
        project = Maxwell2d(project_file, non_graphical=False)

        current_setups = project.get_setups()

        if "user_setup" not in current_setups:
            setup = project.create_setup(name="user_setup", setup_type="Transient")

            user_variables = project.variable_manager.variables
            logger.debug(f"user_variables={user_variables}")

            n0, p = user_variables['n0'].numeric_value, user_variables['p'].numeric_value
            T = 60 / n0 / p

            setup.props['StopTime'] = f"{T * 2}s"
            setup.props['TimeStep'] = f"{T / 100}s"
            setup.update()
            logger.debug(f"优化参数: n0={n0}, p={p}, T={T}")

        project.analyze(setup="user_setup", cores=20, tasks=8, gpus=1)
        project.save_project()

        result = {"status": "success"}
        print(json.dumps(result))

    except Exception as e:
        logger.error(f"优化过程中出错: {e}")
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    project_file = sys.argv[1]
    run_optimization(project_file)
