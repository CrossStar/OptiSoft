from PySide6.QtCore import Slot, QUrl
from PySide6.QtWidgets import QFrame
from views.ui.Ui_modelPage import Ui_modelPage


class ModelWidget(QFrame, Ui_modelPage):
    """模型界面"""

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(" ", "-"))
        self.setupUi(self)

        # 添加选项
        object_items = {
            '平均转矩': "http://127.0.0.1:5632/avgTorque",
            '转矩波动': "http://127.0.0.1:5632/rippleTorque"
        }
        self.comboBox.addItems(object_items.keys())
        self.comboBox.currentIndexChanged.connect(
            self.on_object_combobox_changed)
        self.update_webview_url(object_items[self.comboBox.currentText()])

    @Slot()
    def on_object_combobox_changed(self):
        # 更新 qwebengineview 的 url
        selected_item = self.comboBox.currentText()
        url = {
            '平均转矩': "http://127.0.0.1:5632/avgTorque",
            '转矩波动': "http://127.0.0.1:5632/rippleTorque"
        }.get(selected_item, "about:blank")
        self.update_webview_url(url)

    def update_webview_url(self, url):
        self.webEngineView.setUrl(QUrl(url))
