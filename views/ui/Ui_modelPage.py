# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelPage.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QWidget)

from qfluentwidgets import ComboBox

class Ui_modelPage(object):
    def setupUi(self, modelPage):
        if not modelPage.objectName():
            modelPage.setObjectName(u"modelPage")
        modelPage.resize(1507, 900)
        self.gridLayout_2 = QGridLayout(modelPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.webEngineView = QWebEngineView(modelPage)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 1, 0, 1, 3)

        self.comboBox = ComboBox(modelPage)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(modelPage)

        QMetaObject.connectSlotsByName(modelPage)
    # setupUi

    def retranslateUi(self, modelPage):
        modelPage.setWindowTitle(QCoreApplication.translate("modelPage", u"Form", None))
    # retranslateUi

