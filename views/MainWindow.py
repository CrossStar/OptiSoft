from PySide6 import QtGui
from PySide6.QtGui import QIcon
from ansys.aedt.core import settings
from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FIF

from views.upLoadWindow import UpLoadWidget
from views.codeEditWindow import CodeEditWidget
from views.consoleWindow import ConsoleWidget
from views.upLoadWindow import DataSyncer
from views.consAndGoalWindow import ConsAndGoalWidget
from views.modelWindow import ModelWidget
from views.optimizeWindow import OptimizeWidget

from views.icons.icon import Icon


class MainWindow(FluentWindow):
    """主界面"""

    def __init__(self):
        super().__init__()

        settings.global_log_file_name = "maxwell.log"

        self.data_syncer = DataSyncer()

        self.upLoadInterface = UpLoadWidget("Home Interface", self.data_syncer,
                                            self)
        self.consAndGoalInterface = ConsAndGoalWidget(
            "Cons And Goal Interface", self.data_syncer, self)
        self.codeEditInterface = CodeEditWidget("Code Edit Interface",
                                                self.data_syncer, self)
        self.consoleInterface = ConsoleWidget("Console Interface", self)
        self.modelInterface = ModelWidget("Model Interface", self)
        self.optimizeInterface = OptimizeWidget("Optimize Interface", self)

        self.initNavigation()
        self.initWindow()
        self.center()

    def initNavigation(self):
        self.addSubInterface(self.upLoadInterface, FIF.HOME, "上传文件")
        self.addSubInterface(self.consAndGoalInterface, Icon.LINK, "约束和目标")
        self.addSubInterface(self.codeEditInterface, Icon.CODE, "代码编辑")
        self.addSubInterface(self.modelInterface, FIF.TILES, "代理模型")
        self.addSubInterface(self.optimizeInterface, Icon.TRENDING, "变量优化")
        self.addSubInterface(self.consoleInterface, Icon.CONSOLE, "控制台")

    def initWindow(self):
        self.resize(1420, 915)
        self.setWindowIcon(QIcon(":/qfluentwidgets/images/logo.png"))
        self.setWindowTitle("基于 PySide6 的 Ansys Maxwell 优化软件")
        self.navigationInterface.setExpandWidth(200)

    def center(self):
        screen = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
