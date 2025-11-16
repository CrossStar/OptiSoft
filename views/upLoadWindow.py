import os

from PySide6.QtCore import Signal, Slot, QThread, QObject
from PySide6.QtWidgets import (
    QFrame,
    QTableWidgetItem,
    QHeaderView,
    QFileDialog,
)
from ansys.aedt.core import Maxwell2d
from ansys.aedt.core.aedt_logger import AedtLogger
from qfluentwidgets import FluentIcon

from views.ui.Ui_upLoadPage import Ui_upLoadPage

logger = AedtLogger()


# 中介类，负责信号的传递
class DataSyncer(QObject):
    # 定义一个信号用于发送选中的行索引
    user_project = Signal(Maxwell2d)
    file_path = Signal(str)
    rowsSelected = Signal(list)  # 传递选中的列索引

    user_constraint = Signal(list)  # 传递用户约束
    user_goal = Signal(list)  # 传递用户目标

    def __init__(self):
        super().__init__()


class OpenMaxwell(QThread):
    project_initialized = Signal(Maxwell2d)  # 传递初始化后的Maxwell2d对象

    def __init__(self, file_path):
        super(OpenMaxwell, self).__init__()
        self.file_path = file_path

    def run(self):
        try:
            user_project = Maxwell2d(
                project=self.file_path,
                non_graphical=True,
                close_on_exit=False,
                remove_lock=True,
            )
            user_project.logger.enable_log_on_file()
            self.project_initialized.emit(user_project)  # 发射信号传递user_project
        except Exception as e:
            AedtLogger.error(f"Error: {e}")


class UpLoadWidget(QFrame, Ui_upLoadPage):
    variables_updated = Signal(dict)  # 用于更新变量的信号
    designs_updated = Signal(list)  # 用于更新设计列表的信号

    def __init__(self, text: str, data_syncer: DataSyncer, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(" ", "-"))
        self.setupUi(self)

        self.open_maxwell = None
        self.file_path = None
        self.user_project = None  # 用于保存Maxwell2d项目
        self.user_variables = {}  # 用于保存变量
        self.data_syncer = data_syncer
        self.enable_sync = False

        self.init_table()
        self.init_file_upload_area()
        self.init_preview_area()

        self.browseButton.clicked.connect(self.browseButton_clicked)
        self.upLoadButton.clicked.connect(self.upLoadButton_clicked)
        self.ensureButton.clicked.connect(self.ensureButton_clicked)
        self.chooseVariableButton.clicked.connect(
            self.chooseVariableButton_clicked)

    def init_table(self):
        self.tableWidget.setBorderVisible(True)
        self.tableWidget.setBorderRadius(8)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["参数", "数值", "单位"])
        self.tableWidget.verticalHeader().hide()

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

    def init_file_upload_area(self):
        self.lineEdit.setPlaceholderText(
            "请在这里输入你的 Ansys Maxwell 项目 (*.aedt) 路径")
        self.browseButton.setIcon(FluentIcon.FOLDER)
        self.browseButton.setText("浏览文件")
        self.upLoadButton.setText("上传文件")
        self.upLoadButton.setIcon(FluentIcon.UP)

        self.ensureButton.setText("确认选择设计")
        self.ensureButton.setIcon(FluentIcon.ACCEPT)

        self.chooseVariableButton.setText("请在这里选择你想要优化的变量")
        self.chooseVariableButton.setIcon(FluentIcon.TAG)

        self.comboBox.setPlaceholderText("在选择你的项目后，这里会显示你的设计列表")

    def init_preview_area(self):
        self.previewArea.setStyleSheet(
            "border:1px solid #eaecef; border-radius: 8px;")

    def browseButton_clicked(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "AEDT Files (*.aedt)")
        if self.file_path:
            self.lineEdit.setText(self.file_path)

    def upLoadButton_clicked(self):
        self.comboBox.clear()
        self.open_maxwell = OpenMaxwell(self.file_path)
        self.open_maxwell.start()

        # 连接信号，接收项目初始化后的Maxwell2d对象
        self.open_maxwell.project_initialized.connect(
            self.on_project_initialized)

    @Slot(Maxwell2d)
    def on_project_initialized(self, project: Maxwell2d):
        self.user_project = project
        # 发射设计列表更新信号
        self.update_designs()

    def ensureButton_clicked(self):
        if self.user_project is not None:
            self.user_project.set_active_design(self.comboBox.currentText())
            self.user_variables = self.user_project.variable_manager.variables

            # 更新表格的 parameters 列为 user_variables 的 keys
            self.tableWidget.setRowCount(len(self.user_variables))
            for i, key in enumerate(self.user_variables.keys()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(key))
                self.tableWidget.setItem(
                    i, 1,
                    QTableWidgetItem(
                        str(self.user_variables[key].numeric_value)))
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(self.user_variables[key].units))

            # 更新预览区域
            if not os.path.exists("temp"):
                os.makedirs("temp")
            self.user_project.post.export_model_picture("temp/preview.png",
                                                        orientation="front")
            self.previewArea.setPixmap("temp/preview.png")
            self.previewArea.scaledToHeight(735)
            self.previewArea.setBorderRadius(8, 8, 8, 8)
        else:
            AedtLogger.warning("The project is not initialized yet")

    def chooseVariableButton_clicked(self):
        if self.chooseVariableButton.isChecked():
            self.chooseVariableButton.setText("变量已被选择")
        else:
            self.chooseVariableButton.setText("请在这里选择你想要优化的变量")

        self.enable_sync = self.chooseVariableButton.isChecked()
        logger.debug(f"现在选择变量按钮的状态为：{self.enable_sync}")

        if self.enable_sync:
            selected_rows = []
            selected_indexes = self.tableWidget.selectedIndexes()
            selected_row_nums = sorted(
                set(index.row() for index in selected_indexes))  # 获取选中的行号

            for row in selected_row_nums:
                row_data = [(self.tableWidget.item(row, col).text()
                             if self.tableWidget.item(row, col) else "")
                            for col in range(self.tableWidget.columnCount())]
                selected_rows.append(row_data)

            if selected_rows:
                logger.debug(f"TableA 选中的行数据: {selected_rows}")
                self.data_syncer.rowsSelected.emit(selected_rows)  # 发送完整数据

    def update_designs(self):
        if isinstance(self.user_project, Maxwell2d):
            # 获取设计列表并发射信号
            design_list = self.user_project.design_list
            self.comboBox.addItems(design_list)

            self.data_syncer.user_project.emit(self.user_project)
            self.data_syncer.file_path.emit(self.file_path)
        else:
            AedtLogger.warning("The project is not initialized yet")
