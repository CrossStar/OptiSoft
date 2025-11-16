# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'codeEditPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QSizePolicy, QSpacerItem, QTableWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (PrimaryPushButton, StrongBodyLabel, TableWidget, ToolButton)

class Ui_codeEditPage(object):
    def setupUi(self, codeEditPage):
        if not codeEditPage.objectName():
            codeEditPage.setObjectName(u"codeEditPage")
        codeEditPage.resize(1492, 900)
        self.horizontalLayout = QHBoxLayout(codeEditPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.codeEditorArea = QWidget(codeEditPage)
        self.codeEditorArea.setObjectName(u"codeEditorArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeEditorArea.sizePolicy().hasHeightForWidth())
        self.codeEditorArea.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.codeEditorArea, 0, 0, 4, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.selectedHeader = StrongBodyLabel(codeEditPage)
        self.selectedHeader.setObjectName(u"selectedHeader")

        self.gridLayout.addWidget(self.selectedHeader, 0, 0, 1, 2)

        self.selectedTabView = TableWidget(codeEditPage)
        self.selectedTabView.setObjectName(u"selectedTabView")
        self.selectedTabView.setMinimumSize(QSize(500, 250))
        self.selectedTabView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout.addWidget(self.selectedTabView, 1, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dependentHeaders = StrongBodyLabel(codeEditPage)
        self.dependentHeaders.setObjectName(u"dependentHeaders")

        self.gridLayout_3.addWidget(self.dependentHeaders, 0, 0, 1, 1)

        self.dependentAdd = ToolButton(codeEditPage)
        self.dependentAdd.setObjectName(u"dependentAdd")

        self.gridLayout_3.addWidget(self.dependentAdd, 0, 1, 1, 1)

        self.dependentDelete = ToolButton(codeEditPage)
        self.dependentDelete.setObjectName(u"dependentDelete")

        self.gridLayout_3.addWidget(self.dependentDelete, 0, 2, 1, 1)

        self.dependentTabView = TableWidget(codeEditPage)
        self.dependentTabView.setObjectName(u"dependentTabView")
        self.dependentTabView.setMinimumSize(QSize(500, 100))

        self.gridLayout_3.addWidget(self.dependentTabView, 1, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.goalHeader = StrongBodyLabel(codeEditPage)
        self.goalHeader.setObjectName(u"goalHeader")

        self.gridLayout_7.addWidget(self.goalHeader, 0, 0, 1, 1)

        self.goalAdd = ToolButton(codeEditPage)
        self.goalAdd.setObjectName(u"goalAdd")

        self.gridLayout_7.addWidget(self.goalAdd, 0, 1, 1, 1)

        self.goalDelete = ToolButton(codeEditPage)
        self.goalDelete.setObjectName(u"goalDelete")

        self.gridLayout_7.addWidget(self.goalDelete, 0, 2, 1, 1)

        self.goalTabView = TableWidget(codeEditPage)
        self.goalTabView.setObjectName(u"goalTabView")
        self.goalTabView.setMinimumSize(QSize(500, 100))

        self.gridLayout_7.addWidget(self.goalTabView, 1, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout_7)

        self.startOptimizeButton = PrimaryPushButton(codeEditPage)
        self.startOptimizeButton.setObjectName(u"startOptimizeButton")
        self.startOptimizeButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.startOptimizeButton)


        self.gridLayout_8.addLayout(self.verticalLayout, 0, 2, 4, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_8)


        self.retranslateUi(codeEditPage)

        QMetaObject.connectSlotsByName(codeEditPage)
    # setupUi

    def retranslateUi(self, codeEditPage):
        codeEditPage.setWindowTitle(QCoreApplication.translate("codeEditPage", u"Form", None))
        self.selectedHeader.setText(QCoreApplication.translate("codeEditPage", u"\u5df2\u9009\u62e9\u7684\u72ec\u7acb\u53d8\u91cf\u8868", None))
        self.dependentHeaders.setText(QCoreApplication.translate("codeEditPage", u"\u7ea6\u675f\u53d8\u91cf\u8868", None))
        self.dependentAdd.setText("")
        self.dependentDelete.setText("")
        self.goalHeader.setText(QCoreApplication.translate("codeEditPage", u"\u5f85\u4f18\u5316\u76ee\u6807\u8868", None))
        self.goalAdd.setText("")
        self.goalDelete.setText("")
        self.startOptimizeButton.setText(QCoreApplication.translate("codeEditPage", u"PushButton", None))
    # retranslateUi

