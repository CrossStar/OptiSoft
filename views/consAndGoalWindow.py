import os
import json
import re
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QFrame, QHeaderView, QTableWidgetItem, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from ansys.aedt.core import Maxwell2d
from ansys.aedt.core.aedt_logger import AedtLogger
from qfluentwidgets import FluentIcon, TableWidget, ComboBox
from views.ui.Ui_consAndGoalPage import Ui_consAndGoalPage
from views.upLoadWindow import DataSyncer

logger = AedtLogger()


def read_json_file(file_path: str) -> dict:
    """读取 JSON 文件，若不存在则返回空字典。"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_json_file(file_path: str, data: dict) -> None:
    """将字典写入 JSON 文件。"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def remove_expression_in_json(file_path: str, param: str) -> None:
    """
    从指定 JSON 文件中删除 param 对应的公式。
    不存在文件时忽略。
    """
    expressions = read_json_file(file_path)
    if param in expressions:
        del expressions[param]
        write_json_file(file_path, expressions)


class ExpressionEditor(QWebEngineView):

    def __init__(self, parent):
        super().__init__(parent)
        self.editor_flag = []

        current_dir = os.path.dirname(__file__)
        html_file_path = os.path.join(current_dir, "..", "resource",
                                      "mathlive", "index.html")
        self.setUrl(QUrl.fromLocalFile(os.path.abspath(html_file_path)))
        settings = self.settings()
        settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls,
                              True)

        # 设置 User-Agent 以避免某些CDN拒绝
        self.page().profile().setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        )

    def clear_editor(self):
        """清空 math-field"""
        self.page().runJavaScript(
            "document.querySelector('math-field').setValue('');")

    def get_latex(self, callback):
        """获取 LaTeX 并使用回调返回值"""
        self.page().runJavaScript(
            "document.querySelector('math-field').getValue();", callback)

    def get_acsii_latex(self, latex, callback):
        """获取 ASCII LaTeX 并使用回调返回值"""
        self.page().runJavaScript(
            f"convertLatexToAscii('{latex}');",
            callback,
        )

    def set_latex(self, latex):
        """设置 LaTeX 到 math-field 并手动触发 input 事件"""
        js_code = f"""
        document.querySelector('math-field').setValue({json.dumps(latex)});
        document.querySelector('math-field').dispatchEvent(new Event('input', {{ bubbles: true }}));
        """
        self.page().runJavaScript(js_code)

    def insert_latex(self, latex: str):
        # 利用 json.dumps 自动转义
        latex_json = json.dumps(latex)
        js_code = f"""
        mf.insert({latex_json});
        """
        self.page().runJavaScript(js_code)


class ConsAndGoalWidget(QFrame, Ui_consAndGoalPage):

    def __init__(self, text: str, data_syncer: DataSyncer, parent=None):
        super().__init__(parent)
        self.user_project = None
        self.setObjectName(text.replace(" ", "-"))
        self.setupUi(self)

        # 1. 初始化页面控件
        self.init_tabView()
        self.init_button()
        self.init_combo()
        self.init_expression_edit()

        # 2. 绑定信号/槽
        self.selectedTabView.clicked.connect(self.update_expression)
        self.data_syncer = data_syncer
        self.data_syncer.rowsSelected.connect(self.update_selected_table_rows)
        self.data_syncer.user_project.connect(self.get_user_project)
        self.data_syncer.file_path.connect(self.get_file_path)

        # 当 constraintTabView 选中某行时，尝试从 cons.json 加载表达式
        self.constraintTabView.itemSelectionChanged.connect(
            lambda: self.load_expression_from_file(self.constraintTabView,
                                                   "./temp/cons.json"))
        # 当 goalTabView 选中某行时，尝试从 goal.json 加载表达式
        self.goalTabView.itemSelectionChanged.connect(
            lambda: self.load_expression_from_file(self.goalTabView,
                                                   "./temp/goal.json"))

    def init_tabView(self):
        """初始化表格样式"""

        def set_table_properties(table, headers):
            table.setBorderVisible(True)
            table.setBorderRadius(8)
            table.setWordWrap(False)
            table.setColumnCount(len(headers))
            table.setHorizontalHeaderLabels(headers)
            table.verticalHeader().hide()
            for i in range(len(headers)):
                table.horizontalHeader().setSectionResizeMode(
                    i, QHeaderView.ResizeMode.Stretch)

        set_table_properties(self.selectedTabView, ["参数", "数值", "单位"])
        set_table_properties(self.constraintTabView, ["别名", "最大值", "最小值"])
        set_table_properties(self.goalTabView, ["表达式", "最大化？", "权重"])

    def init_combo(self):
        """初始化下拉框"""
        self.quantityCategory.setPlaceholderText("选择工程量类别")
        self.quantityItem.setPlaceholderText("选择类别下的工程量")
        self.quantityCategory.currentIndexChanged.connect(
            self.update_quantity_items)
        self.quantityItem.activated.connect(self.update_expression)

    def update_quantity_items(self):
        """更新工程量类别下的工程量"""
        category = self.quantityCategory.currentText()
        items = self.user_project.post.available_report_quantities(
            quantities_category=category)
        self.quantityItem.clear()
        self.quantityItem.addItems(items)

    def update_expression(self):
        if isinstance(self.sender(), TableWidget):
            selected_items = self.selectedTabView.selectedItems()
            if not selected_items:
                return
            param = selected_items[0].text()
        elif isinstance(self.sender(), ComboBox):
            param = self.quantityItem.currentText()
        else:
            return

        self.editor.insert_latex(f"\\;\\mathbf{{{param}}}")

    def update_selected_table_rows(self, selected_rows):
        """更新选中的行数据"""
        self.selectedTabView.setRowCount(len(selected_rows))
        for row_index, row_data in enumerate(selected_rows):
            for col_index, cell_value in enumerate(row_data):
                self.selectedTabView.setItem(row_index, col_index,
                                             QTableWidgetItem(cell_value))

    def get_user_project(self, user_project: Maxwell2d):
        """获取用户项目并加载对应的工程量类别"""
        self.user_project = user_project
        if isinstance(self.user_project, Maxwell2d):
            categories = self.user_project.post.available_quantities_categories(
            )
            self.quantityCategory.addItems(categories)

    def get_file_path(self, file_path):
        """获取文件路径（如有必要可在此处继续使用）"""
        self.file_path = file_path

    def init_button(self):
        """初始化按钮"""
        self.joinConsButton.setIcon(FluentIcon.RIGHT_ARROW)
        self.joinGoalButton.setIcon(FluentIcon.RIGHT_ARROW)
        self.consDeleteButton.setIcon(FluentIcon.DELETE)
        self.goalDeleteButton.setIcon(FluentIcon.DELETE)

        # 点击删除按钮时，从对应表格和 JSON 同步删除
        self.consDeleteButton.clicked.connect(
            lambda: self.remove_selected_row_and_expression(
                self.constraintTabView, "./temp/cons.json"))
        self.goalDeleteButton.clicked.connect(
            lambda: self.remove_selected_row_and_expression(
                self.goalTabView, "./temp/goal.json"))

        # 连接按钮点击信号，并显式传递按钮对象
        self.joinConsButton.clicked.connect(lambda: self.join_cons_goal(
            self.joinConsButton, self.constraintTabView, "./temp/cons.json"))
        self.joinGoalButton.clicked.connect(lambda: self.join_cons_goal(
            self.joinGoalButton, self.goalTabView, "./temp/goal.json"))

        self.consReadyButton.clicked.connect(self.on_cons_ready)
        self.goalReadyButton.clicked.connect(self.on_goal_ready)

    def on_cons_ready(self):
        # 读取 consTabView 中的数据
        cons = []
        for row in range(self.constraintTabView.rowCount()):
            cons.append({
                "cons": self.constraintTabView.item(row, 0).text(),
                "max": self.constraintTabView.item(row, 1).text(),
                "min": self.constraintTabView.item(row, 2).text(),
            })

        self.data_syncer.user_constraint.emit(cons)

    def on_goal_ready(self):
        # 读取 goalTabView 中的数据
        goal = []
        for row in range(self.goalTabView.rowCount()):
            goal.append({
                "goal": self.goalTabView.item(row, 0).text(),
                "isMaximize": self.goalTabView.item(row, 1).text(),
                "weight": self.goalTabView.item(row, 2).text(),
            })

        self.data_syncer.user_goal.emit(goal)

    def join_cons_goal(self, button, tab, file_path):
        """从编辑器中获取 LaTeX 公式后，调用保存并更新表格"""
        if button == self.joinConsButton:
            self.editor.get_latex(lambda latex: self.save_latex_to_file(
                latex, file_path, tab, check_equal=True))
        elif button == self.joinGoalButton:
            self.editor.get_latex(lambda latex: self.save_latex_to_file(
                latex, file_path, tab, check_equal=False))

    def save_latex_to_file(self, latex, file_path, tab, check_equal=True):
        """
        将 LaTeX 公式保存到指定 JSON 文件，并同步更新表格。
        :param check_equal: 为 True 时，需使用 '=' 分隔（用在约束场景）；
                        为 False 时，表示目标场景不再强制要求有 '='。
        """
        latex = latex.strip()
        if not latex:
            logger.error("表达式为空，请在编辑器中输入表达式后再点击『加入』按钮。")
            return

        expressions = read_json_file(file_path)

        if check_equal:
            # 约束逻辑：必须有 '='
            if "=" not in latex:
                logger.error("公式格式不正确，请使用“参数 = 表达式”的格式来定义约束。")
                return
            param, expression = latex.split("=", 1)
            param = param.strip()
            expression = expression.strip()

            # 写入到 JSON
            expressions[param] = expression
            write_json_file(file_path, expressions)

            # 在 constraintTabView 中插入新行
            if tab == self.constraintTabView:
                row_count = tab.rowCount()
                tab.insertRow(row_count)
                tab.setItem(row_count, 0, QTableWidgetItem(param))
                tab.setItem(row_count, 1, QTableWidgetItem(""))  # 最大值
                tab.setItem(row_count, 2, QTableWidgetItem(""))  # 最小值

                # 这一步是将 ASCII latex（例如 a=b*c）转换成能被 AEDT 接受的公式，再创建输出变量
                self.editor.get_acsii_latex(
                    latex,
                    lambda ascii_latex: self.process_ascii_latex(ascii_latex),
                )

        else:
            # 目标逻辑：不强制 '='，但也写入 JSON
            expression = latex  # 这里就是目标的整体表达式
            # 这里直接以 expression 作为 key 和 value，也可根据需要自定义 key
            expressions[expression] = expression
            write_json_file(file_path, expressions)

            if tab == self.goalTabView:
                row_count = tab.rowCount()
                tab.insertRow(row_count)
                tab.setItem(row_count, 0, QTableWidgetItem(expression))  # 表达式
                tab.setItem(row_count, 1, QTableWidgetItem(""))  # 是否最大化
                tab.setItem(row_count, 2, QTableWidgetItem(""))  # 权重

        # 清空编辑器内容
        self.editor.clear_editor()

    def process_ascii_latex(self, ascii_latex):
        # 使用正则表达式去除 bb "" 部分
        ascii_latex = re.sub(r'bb\s*"([^"]*)"', r"\1", ascii_latex)

        param, expression = ascii_latex.split("=", 1)
        param = param.strip().replace(" ", "")
        expression = expression.strip()
        self.user_project.create_output_variable(variable=param,
                                                 expression=expression)
        self.user_project.save_project()

    def remove_selected_row_and_expression(self, tab, file_path):
        """
        删除当前选中行并同步删除 JSON 中记录。
        """
        row = tab.currentRow()
        if row >= 0:
            param_item = tab.item(row, 0)
            if param_item:
                param = param_item.text()
                # 先删除表格中的行
                tab.removeRow(row)
                # 再删除 JSON 中的对应记录
                remove_expression_in_json(file_path, param)

    def load_expression_from_file(self, tab, file_path):
        """
        当用户选中表格某行时，从 JSON 中读取对应的表达式并设置到编辑器中显示。
        """
        if tab == self.constraintTabView:
            selected_items = tab.selectedItems()
            if not selected_items:
                return
            param = selected_items[0].text()

            expressions = read_json_file(file_path)
            expression = expressions.get(param, "")

            if expression:
                self.editor.set_latex(f"{param} = {expression}")
            else:
                self.editor.clear_editor()
        elif tab == self.goalTabView:
            selected_items = tab.selectedItems()
            if not selected_items:
                return
            expression = selected_items[0].text()

            self.editor.set_latex(expression)

    def init_expression_edit(self):
        """初始化 math-field 编辑器并将其替换到界面上"""
        self.editor = ExpressionEditor(self)
        parent_layout = self.expressionEditArea.parentWidget().layout()
        if parent_layout is None:
            raise RuntimeError("expressionEditArea 没有父布局，无法替换！")

        parent_layout.replaceWidget(self.expressionEditArea, self.editor)
        self.editor.setSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        self.editor.setStyleSheet(
            "border:1px solid #eaecef; border-radius: 8px;")
