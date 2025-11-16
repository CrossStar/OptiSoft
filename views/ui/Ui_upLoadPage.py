# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upLoadPage.ui'
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

from qfluentwidgets import (ComboBox, ImageLabel, LineEdit, PrimaryPushButton,
    PushButton, TableWidget, TransparentTogglePushButton)
import resource_rc

class Ui_upLoadPage(object):
    def setupUi(self, upLoadPage):
        if not upLoadPage.objectName():
            upLoadPage.setObjectName(u"upLoadPage")
        upLoadPage.resize(1296, 895)
        self.verticalLayout = QVBoxLayout(upLoadPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upLoadArea = QWidget(upLoadPage)
        self.upLoadArea.setObjectName(u"upLoadArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upLoadArea.sizePolicy().hasHeightForWidth())
        self.upLoadArea.setSizePolicy(sizePolicy)
        self.upLoadArea.setMinimumSize(QSize(0, 120))
        self.upLoadArea.setMaximumSize(QSize(16777215, 140))
        self.upLoadArea.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.upLoadArea)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 7, 1, 1)

        self.lineEdit = LineEdit(self.upLoadArea)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(1000, 16777215))

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)

        self.browseButton = PushButton(self.upLoadArea)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy2)
        self.browseButton.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.browseButton, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.upLoadButton = PrimaryPushButton(self.upLoadArea)
        self.upLoadButton.setObjectName(u"upLoadButton")
        sizePolicy2.setHeightForWidth(self.upLoadButton.sizePolicy().hasHeightForWidth())
        self.upLoadButton.setSizePolicy(sizePolicy2)
        self.upLoadButton.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.upLoadButton, 0, 7, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 4, 1, 1)

        self.ensureButton = PrimaryPushButton(self.upLoadArea)
        self.ensureButton.setObjectName(u"ensureButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ensureButton.sizePolicy().hasHeightForWidth())
        self.ensureButton.setSizePolicy(sizePolicy3)
        self.ensureButton.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.ensureButton, 2, 5, 1, 3)

        self.comboBox = ComboBox(self.upLoadArea)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 2)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.upLoadArea)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = TableWidget(upLoadPage)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setMinimumSize(QSize(300, 0))
        self.tableWidget.setMaximumSize(QSize(500, 16777215))
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.chooseVariableButton = TransparentTogglePushButton(upLoadPage)
        self.chooseVariableButton.setObjectName(u"chooseVariableButton")
        self.chooseVariableButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.chooseVariableButton, 1, 0, 1, 1)

        self.previewArea = ImageLabel(upLoadPage)
        self.previewArea.setObjectName(u"previewArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.previewArea.sizePolicy().hasHeightForWidth())
        self.previewArea.setSizePolicy(sizePolicy5)
        self.previewArea.setMaximumSize(QSize(735, 16777215))

        self.gridLayout_2.addWidget(self.previewArea, 0, 2, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(upLoadPage)

        QMetaObject.connectSlotsByName(upLoadPage)
    # setupUi

    def retranslateUi(self, upLoadPage):
        upLoadPage.setWindowTitle(QCoreApplication.translate("upLoadPage", u"Form", None))
        self.browseButton.setText(QCoreApplication.translate("upLoadPage", u"PushButton", None))
        self.upLoadButton.setText(QCoreApplication.translate("upLoadPage", u"PushButton", None))
        self.ensureButton.setText(QCoreApplication.translate("upLoadPage", u"PushButton", None))
        self.chooseVariableButton.setText(QCoreApplication.translate("upLoadPage", u"PushButton", None))
        self.previewArea.setText("")
    # retranslateUi

