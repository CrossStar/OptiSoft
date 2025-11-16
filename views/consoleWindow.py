import os
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QFrame, QApplication
from PySide6.QtGui import QFont
from views.ui.Ui_consolePage import Ui_consolePage


class ConsoleWidget(QFrame, Ui_consolePage):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(" ", "-"))
        self.setupUi(self)

        # 设置日志文件路径
        self.log_file_path = os.path.expanduser(
            r"~\AppData\Local\Temp\maxwell.log")
        print(self.log_file_path)

        # 创建定时器，每隔100ms检查一次日志文件
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_log_file)
        self.timer.start(100)  # 100ms 检查一次

        self.last_content = ""
        self.set_font()

        app = QApplication.instance()
        app.aboutToQuit.connect(self.add_separator)

    def set_font(self):
        """设置控制台的字体为 Consolas，字号为 15"""
        font = QFont("Consolas")
        font.setPointSize(15)
        self.console.setFont(font)

    @Slot()
    def check_log_file(self):
        """检查日志文件是否有新的内容"""
        if os.path.exists(self.log_file_path):
            with open(self.log_file_path, "r") as file:
                content = file.read()
                if content != self.last_content:
                    self.last_content = content
                    self.update_console(content)

    def update_console(self, new_content: str):
        """更新控制台内容，设置markdown格式并根据内容设置颜色"""
        markdown_lines = []
        for line in new_content.splitlines():
            if "INFO" in line:
                line = "<font color='green'>" + line + "</font>"
            elif "ERROR" in line:
                line = "<font color='red'>" + line + "</font>"
            elif "WARNING" in line:
                line = "<font color='#ffcb19'>" + line + "</font>"
            markdown_lines.append(line)

        self.console.setMarkdown("\n\n".join(markdown_lines))

    def add_separator(self):
        """在日志文件末尾添加分隔符"""
        if self.last_content and os.path.exists(self.log_file_path):
            with open(self.log_file_path, "a") as file:
                file.write("\n\n---\n\n")

    def scroll_to_bottom(self):
        """确保滚动条滚动到底部"""
        self.console.verticalScrollBar().setValue(
            self.console.verticalScrollBar().maximum())
