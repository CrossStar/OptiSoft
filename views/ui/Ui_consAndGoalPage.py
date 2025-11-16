# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consAndGoalPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, PrimaryPushButton, TableWidget,
    ToolButton)

class Ui_consAndGoalPage(object):
    def setupUi(self, consAndGoalPage):
        if not consAndGoalPage.objectName():
            consAndGoalPage.setObjectName(u"consAndGoalPage")
        consAndGoalPage.resize(1420, 915)
        self.horizontalLayout = QHBoxLayout(consAndGoalPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = BodyLabel(consAndGoalPage)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.label)

        self.selectedTabView = TableWidget(consAndGoalPage)
        self.selectedTabView.setObjectName(u"selectedTabView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectedTabView.sizePolicy().hasHeightForWidth())
        self.selectedTabView.setSizePolicy(sizePolicy1)
        self.selectedTabView.setMinimumSize(QSize(400, 500))
        self.selectedTabView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.selectedTabView)

        self.label_2 = BodyLabel(consAndGoalPage)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.label_2)

        self.quantityCategory = ComboBox(consAndGoalPage)
        self.quantityCategory.setObjectName(u"quantityCategory")
        self.quantityCategory.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.quantityCategory)

        self.quantityItem = ComboBox(consAndGoalPage)
        self.quantityItem.setObjectName(u"quantityItem")
        self.quantityItem.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.quantityItem)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.joinConsButton = PrimaryPushButton(consAndGoalPage)
        self.joinConsButton.setObjectName(u"joinConsButton")
        self.joinConsButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.joinConsButton)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.expressionEditArea = QWidget(consAndGoalPage)
        self.expressionEditArea.setObjectName(u"expressionEditArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.expressionEditArea.sizePolicy().hasHeightForWidth())
        self.expressionEditArea.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.expressionEditArea)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.joinGoalButton = PrimaryPushButton(consAndGoalPage)
        self.joinGoalButton.setObjectName(u"joinGoalButton")
        self.joinGoalButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.joinGoalButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.consReadyButton = QPushButton(consAndGoalPage)
        self.consReadyButton.setObjectName(u"consReadyButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.consReadyButton.sizePolicy().hasHeightForWidth())
        self.consReadyButton.setSizePolicy(sizePolicy3)
        self.consReadyButton.setMinimumSize(QSize(0, 36))

        self.gridLayout_2.addWidget(self.consReadyButton, 0, 1, 1, 1)

        self.constraintTabView = TableWidget(consAndGoalPage)
        self.constraintTabView.setObjectName(u"constraintTabView")
        self.constraintTabView.setMinimumSize(QSize(400, 0))

        self.gridLayout_2.addWidget(self.constraintTabView, 1, 0, 1, 3)

        self.label_3 = BodyLabel(consAndGoalPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.consDeleteButton = ToolButton(consAndGoalPage)
        self.consDeleteButton.setObjectName(u"consDeleteButton")

        self.gridLayout_2.addWidget(self.consDeleteButton, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.goalReadyButton = QPushButton(consAndGoalPage)
        self.goalReadyButton.setObjectName(u"goalReadyButton")
        sizePolicy3.setHeightForWidth(self.goalReadyButton.sizePolicy().hasHeightForWidth())
        self.goalReadyButton.setSizePolicy(sizePolicy3)
        self.goalReadyButton.setMinimumSize(QSize(0, 36))

        self.gridLayout.addWidget(self.goalReadyButton, 0, 1, 1, 1)

        self.goalDeleteButton = ToolButton(consAndGoalPage)
        self.goalDeleteButton.setObjectName(u"goalDeleteButton")

        self.gridLayout.addWidget(self.goalDeleteButton, 0, 2, 1, 1)

        self.goalTabView = TableWidget(consAndGoalPage)
        self.goalTabView.setObjectName(u"goalTabView")

        self.gridLayout.addWidget(self.goalTabView, 1, 0, 1, 3)

        self.label_4 = BodyLabel(consAndGoalPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(consAndGoalPage)

        QMetaObject.connectSlotsByName(consAndGoalPage)
    # setupUi

    def retranslateUi(self, consAndGoalPage):
        consAndGoalPage.setWindowTitle(QCoreApplication.translate("consAndGoalPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("consAndGoalPage", u"\u5df2\u9009\u62e9\u7684\u72ec\u7acb\u53c2\u6570", None))
        self.label_2.setText(QCoreApplication.translate("consAndGoalPage", u"\u9009\u62e9\u5de5\u7a0b\u91cf\u4ee5\u6dfb\u52a0\u7ea6\u675f\u548c\u76ee\u6807", None))
        self.joinConsButton.setText(QCoreApplication.translate("consAndGoalPage", u"\u6dfb\u52a0\u5230\u7ea6\u675f\u53d8\u91cf", None))
        self.joinGoalButton.setText(QCoreApplication.translate("consAndGoalPage", u"\u6dfb\u52a0\u5230\u76ee\u6807\u53d8\u91cf", None))
        self.consReadyButton.setText(QCoreApplication.translate("consAndGoalPage", u"\u786e\u5b9a", None))
        self.label_3.setText(QCoreApplication.translate("consAndGoalPage", u"\u7ea6\u675f\u53d8\u91cf\u8868", None))
        self.consDeleteButton.setText("")
        self.goalReadyButton.setText(QCoreApplication.translate("consAndGoalPage", u"\u786e\u5b9a", None))
        self.goalDeleteButton.setText("")
        self.label_4.setText(QCoreApplication.translate("consAndGoalPage", u"\u76ee\u6807\u53d8\u91cf\u8868", None))
    # retranslateUi

