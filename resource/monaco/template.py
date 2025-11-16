'''
Author: Zhixin Wu && wuzhixin.321@qq.com
Date: 2025-03-01 15:51:18
LastEditTime: 2025-03-01 16:00:58

Copyright (c) 2025 by wuzhixin.321@qq.com, All Rights Reserved. 
'''

import os

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QFrame, QHeaderView, QTableWidgetItem, QSizePolicy, QVBoxLayout
from qfluentwidgets import FluentIcon

from views.ui.Ui_codeEditPage import Ui_codeEditPage
from views.upLoadWindow import DataSyncer


class Editor(QWebEngineView):
    def __init__(self, par):
        super().__init__(par)
        self.editor_flag = []

        current_dir = os.path.dirname(__file__)
        html_file_path = os.path.join(current_dir, '..', 'resource', 'monaco', 'index.html')
        absolute_path = os.path.abspath(html_file_path)
        print(absolute_path)
        self.setUrl(QUrl.fromLocalFile(absolute_path))

    def get_value(self, callback):
        self.page().runJavaScript("monaco.editor.getModels()[0].getValue()", callback)

    def set_value(self, data):
        import base64
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.page().runJavaScript("monaco.editor.getModels()[0].setValue(Base.decode('{}'))".format(data))

    def change_language(self, lan):
        self.page().runJavaScript("monaco.editor.setModelLanguage(monaco.editor.getModels()[0],'{}')".format(lan))

class CodeEditWidget(QFrame, Ui_codeEditPage):
    def __init__(self, text: str, data_syncer: DataSyncer, parent=None):
        super().__init__(parent=parent)
        self.editor = None
        self.setObjectName(text.replace(' ', '-'))
        self.setupUi(self)

        self.init_codeEditor()
        self.init_tabView()
        self.init_button()

        self.data_syncer = data_syncer
        self.data_syncer.rowsSelected.connect(self.update_selected_table_rows)

    def init_codeEditor(self):
        self.editor = Editor(self)
        # 创建布局 self.codeEditorArea 的布局
        layout = QVBoxLayout()
        self.codeEditorArea.setLayout(layout)
        layout.addWidget(self.editor)
        self.editor.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.editor.setStyleSheet("border:1px solid #eaecef; border-radius: 8px;")

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

        set_table_properties(self.selectedTabView, ['参数', '数值', '单位'])
        set_table_properties(self.dependentTabView, ['自定义参数', '表达式', '最小值', '最大值'])
        self.dependentTabView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        set_table_properties(self.goalTabView, ['目标参数', '目标值', '权重'])
        
    def update_selected_table_rows(self, selected_rows):
        # 把 selected_rows 填充到 self.selectedTabView 中
        self.selectedTabView.setRowCount(len(selected_rows))  # 设定行数

        for row_index, row_data in enumerate(selected_rows):
            for col_index, cell_value in enumerate(row_data):
                self.selectedTabView.setItem(row_index, col_index, QTableWidgetItem(cell_value))

    def init_button(self):
        self.dependentAdd.setIcon(FluentIcon.ADD)
        self.dependentDelete.setIcon(FluentIcon.DELETE)
        self.goalAdd.setIcon(FluentIcon.ADD)
        self.goalDelete.setIcon(FluentIcon.DELETE)

        self.startOptimizeButton.setText('开始优化')
        self.startOptimizeButton.setIcon(FluentIcon.PLAY)

        self.dependentAdd.clicked.connect(lambda: self.dependentTabView.insertRow(self.dependentTabView.rowCount()))
        self.dependentDelete.clicked.connect(lambda: self.dependentTabView.removeRow(
            self.dependentTabView.currentRow()) if self.dependentTabView.currentRow() >= 0 else None)

        self.goalAdd.clicked.connect(lambda: self.goalTabView.insertRow(self.goalTabView.rowCount()))
        self.goalDelete.clicked.connect(lambda: self.goalTabView.removeRow(
            self.goalTabView.currentRow()) if self.goalTabView.currentRow() >= 0 else None)