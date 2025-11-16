import json
import os
import sys

from PySide6.QtCore import QUrl, QProcess
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QFrame,
    QHeaderView,
    QTableWidgetItem,
    QSizePolicy,
)
from ansys.aedt.core import Maxwell2d
from ansys.aedt.core.aedt_logger import AedtLogger
from qfluentwidgets import FluentIcon

from views.ui.Ui_codeEditPage import Ui_codeEditPage
from views.upLoadWindow import DataSyncer

logger = AedtLogger()


class Editor(QWebEngineView):

    def __init__(self, par):
        super().__init__(par)
        self.editor_flag = []

        current_dir = os.path.dirname(__file__)
        html_file_path = os.path.join(current_dir, "..", "resource", "monaco",
                                      "index.html")
        absolute_path = os.path.abspath(html_file_path)
        print(absolute_path)
        self.setUrl(QUrl.fromLocalFile(absolute_path))

    def get_value(self, callback):
        self.page().runJavaScript("monaco.editor.getModels()[0].getValue()",
                                  callback)

    def set_value(self, data):
        import base64

        data = base64.b64encode(data.encode())
        data = data.decode()
        self.page().runJavaScript(
            "monaco.editor.getModels()[0].setValue(Base.decode('{}'))".format(
                data))

    def change_language(self, lan):
        self.page().runJavaScript(
            "monaco.editor.setModelLanguage(monaco.editor.getModels()[0],'{}')"
            .format(lan))


class CodeEditWidget(QFrame, Ui_codeEditPage):

    def __init__(self, text: str, data_syncer: DataSyncer, parent=None):
        super().__init__(parent=parent)
        self.file_path = None
        self.start_optimize = None
        self.user_project = None
        self.editor = None

        self.user_constraint = None
        self.user_goal = None

        self.setObjectName(text.replace(" ", "-"))
        self.setupUi(self)

        self.init_codeEditor()
        self.init_tabView()
        self.init_button()

        self.data_syncer = data_syncer
        self.data_syncer.rowsSelected.connect(self.update_selected_table_rows)
        self.data_syncer.user_project.connect(self.get_user_project)
        self.data_syncer.file_path.connect(self.get_file_path)

        self.data_syncer.user_constraint.connect(self.get_user_constraint)
        self.data_syncer.user_goal.connect(self.get_user_goal)

    def get_user_constraint(self, user_constraint: list):
        self.user_constraint = user_constraint
        logger.info(f"用户约束为：{self.user_constraint}")

    def get_user_goal(self, user_goal: list):
        self.user_goal = user_goal
        logger.info(f"用户目标为：{self.user_goal}")

    def init_codeEditor(self):
        self.editor = Editor(self)
        # 1. 获取 `codeEditorArea` 的父级布局
        parent_layout = self.codeEditorArea.parentWidget().layout()
        if parent_layout is None:
            raise RuntimeError("codeEditorArea 没有父布局，无法替换！")

        parent_layout.replaceWidget(self.codeEditorArea, self.editor)
        self.editor.setSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        self.editor.setStyleSheet(
            "border:1px solid #eaecef; border-radius: 8px;")

    def init_tabView(self):

        def set_table_properties(table, table_headers: list):
            table.setBorderVisible(True)
            table.setBorderRadius(8)
            table.setWordWrap(False)

            table.setColumnCount(len(table_headers))
            table.setHorizontalHeaderLabels(table_headers)
            table.verticalHeader().hide()
            header = table.horizontalHeader()

            for i in range(len(table_headers)):
                header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        set_table_properties(self.selectedTabView, ["参数", "数值", "单位"])
        set_table_properties(self.dependentTabView,
                             ["自定义参数", "表达式", "最小值", "最大值"])
        self.dependentTabView.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeMode.Interactive)
        set_table_properties(self.goalTabView, ["目标参数", "目标值", "权重"])

    def update_selected_table_rows(self, selected_rows):
        # 把 selected_rows 填充到 self.selectedTabView 中
        self.selectedTabView.setRowCount(len(selected_rows))  # 设定行数

        for row_index, row_data in enumerate(selected_rows):
            for col_index, cell_value in enumerate(row_data):
                self.selectedTabView.setItem(row_index, col_index,
                                             QTableWidgetItem(cell_value))

    def get_user_project(self, user_project):
        self.user_project = user_project

    def get_file_path(self, file_path):
        self.file_path = file_path

    def init_button(self):
        self.dependentAdd.setIcon(FluentIcon.ADD)
        self.dependentDelete.setIcon(FluentIcon.DELETE)
        self.goalAdd.setIcon(FluentIcon.ADD)
        self.goalDelete.setIcon(FluentIcon.DELETE)

        self.startOptimizeButton.setText("开始优化")
        self.startOptimizeButton.setIcon(FluentIcon.PLAY)
        self.startOptimizeButton.clicked.connect(self.startOptimize)

        self.dependentAdd.clicked.connect(
            lambda: self.dependentTabView.insertRow(self.dependentTabView.
                                                    rowCount()))
        self.dependentDelete.clicked.connect(lambda: (
            self.dependentTabView.removeRow(self.dependentTabView.currentRow())
            if self.dependentTabView.currentRow() >= 0 else None))

        self.goalAdd.clicked.connect(
            lambda: self.goalTabView.insertRow(self.goalTabView.rowCount()))
        self.goalDelete.clicked.connect(
            lambda: (self.goalTabView.removeRow(self.goalTabView.currentRow())
                     if self.goalTabView.currentRow() >= 0 else None))

    def startOptimize(self):
        """启动优化任务（QProcess 方式）"""
        if self.user_project is None:
            logger.error(msg="用户项目未初始化，无法优化")
            return

        # 获取当前 Python 解释器路径
        python_executable = sys.executable  # 获取当前 Python 解释器

        # 启动独立进程
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_process_output)
        self.process.readyReadStandardError.connect(self.on_process_error)
        self.process.finished.connect(self.on_process_finished)

        logger.info(msg="启动优化进程...")
        logger.debug(f"{self.file_path}")
        self.process.start(python_executable,
                           ["scripts/run_optimize.py", self.file_path])

    def on_process_output(self):
        """处理子进程的标准输出"""
        output = self.process.readAllStandardOutput().data().decode().strip()
        if output:
            try:
                result = json.loads(output)  # 解析 JSON
                if result.get("status") == "success":
                    logger.info(msg="优化任务成功完成")
                else:
                    logger.error(msg=f"优化失败: {result.get('message', '未知错误')}")
            except json.JSONDecodeError:
                logger.info(msg=f"子进程输出: {output}")

    def on_process_error(self):
        """处理子进程的错误输出"""
        error = self.process.readAllStandardError().data().decode().strip()
        if error:
            logger.error(msg=f"子进程错误: {error}")

    def on_process_finished(self, exitCode, exitStatus):
        """任务完成后回调"""
        if exitCode == 0:
            logger.info(msg="优化完成！")
            self.user_project = Maxwell2d(self.file_path)
            logger.info(
                f"所有 Quantities 为：{self.user_project.post.available_quantities_categories()}"
            )
        else:
            logger.error(msg="优化失败！")
