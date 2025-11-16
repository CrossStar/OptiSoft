import sys
import requests
from PySide6.QtCore import Qt, QThread, Signal, Slot, QUrl
from PySide6.QtWidgets import QApplication, QFrame, QTableWidgetItem, QHeaderView
from views.ui.Ui_optimizePage import Ui_optimizePage


class RequestThread(QThread):
    finished = Signal(bool, int, str, dict)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        results = {}
        try:
            res = requests.post(self.url, timeout=600)
            if res.ok:
                data = res.json()
                message = data.get("message", "无返回消息")
                results = data
                self.finished.emit(True, res.status_code, message, results)
            else:
                self.finished.emit(False, res.status_code, "请求失败", results)
        except Exception as e:
            self.finished.emit(False, 0, f"请求异常: {e}", results)


class OptimizeWidget(QFrame, Ui_optimizePage):

    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setObjectName(text.replace(" ", "-"))
        self.setupUi(self)

        self.optimizerButton.clicked.connect(self.start_optimizer)
        self.paretoPlot.setUrl(QUrl("about:blank"))

    @Slot()
    def start_optimizer(self):
        self.optimizerButton.setEnabled(False)
        self.optimizerButton.setText("优化中...")
        self.optimizerButton.setCursor(Qt.WaitCursor)

        # 构造请求 URL
        n_gen = self.gen.text()
        n_pop = self.pop.text()
        if n_gen and n_pop:
            url = f"http://127.0.0.1:5632/api/start_optimization?n_gen={n_gen}&n_pop={n_pop}"
        else:
            url = "http://127.0.0.1:5632/api/start_optimization"

        # 启动线程发起请求
        self.thread = RequestThread(url)
        self.thread.finished.connect(self.on_request_finished)
        self.thread.start()

    @Slot(bool, int, str, dict)
    def on_request_finished(self, success, status_code, message, results):
        if success:
            print(f"优化任务成功: {message}")
            self.update_result_table(results)
            self.paretoPlot.setUrl(QUrl("http://127.0.0.1:5632/pareto_front"))
        else:
            print(f"优化任务启动失败，状态码：{status_code}，信息：{message}")

        self.optimizerButton.setEnabled(True)
        self.optimizerButton.setText("开始优化")
        self.optimizerButton.setCursor(Qt.PointingHandCursor)

    def update_result_table(self, results):
        """
        更新优化结果表格：
        - 表头：特征名 + 平均转矩 + 转矩波动
        - 内容：对应的 X 和 F 数据
        """
        feature_names = results.get("feature_names", [])
        X = results.get("X", [])
        F = results.get("F", [])

        if not feature_names or not X or not F:
            print("结果数据缺失，无法更新表格。")
            return

        columns = feature_names + ["平均转矩", "转矩波动"]
        self.optimizeResultTable.clear()
        self.optimizeResultTable.setColumnCount(len(columns))
        self.optimizeResultTable.setHorizontalHeaderLabels(columns)
        self.optimizeResultTable.setRowCount(len(X))

        header = self.optimizeResultTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for row_idx, (x_values, f_values) in enumerate(zip(X, F)):
            for col_idx, value in enumerate(x_values):
                item = QTableWidgetItem(f"{value:.2f}")
                self.optimizeResultTable.setItem(row_idx, col_idx, item)
            avg_torque_item = QTableWidgetItem(f"{f_values[0]:.4f}")
            self.optimizeResultTable.setItem(row_idx, len(x_values),
                                             avg_torque_item)
            ripple_item = QTableWidgetItem(f"{f_values[1]:.4f}")
            self.optimizeResultTable.setItem(row_idx,
                                             len(x_values) + 1, ripple_item)

        print("表格已更新完成。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OptimizeWidget("优化器")
    window.show()
    sys.exit(app.exec())
