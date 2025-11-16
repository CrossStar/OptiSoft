# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optimizePage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QSpacerItem, QTableWidgetItem, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PrimaryPushButton, TableWidget)

class Ui_optimizePage(object):
    def setupUi(self, optimizePage):
        if not optimizePage.objectName():
            optimizePage.setObjectName(u"optimizePage")
        optimizePage.resize(1277, 900)
        self.gridLayout = QGridLayout(optimizePage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gen = LineEdit(optimizePage)
        self.gen.setObjectName(u"gen")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen.sizePolicy().hasHeightForWidth())
        self.gen.setSizePolicy(sizePolicy)
        self.gen.setMinimumSize(QSize(500, 40))
        self.gen.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.gen, 0, 3, 1, 1)

        self.label_2 = BodyLabel(optimizePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.pop = LineEdit(optimizePage)
        self.pop.setObjectName(u"pop")
        sizePolicy.setHeightForWidth(self.pop.sizePolicy().hasHeightForWidth())
        self.pop.setSizePolicy(sizePolicy)
        self.pop.setMinimumSize(QSize(500, 40))
        self.pop.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.pop, 1, 3, 1, 1)

        self.label = BodyLabel(optimizePage)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.optimizerButton = PrimaryPushButton(optimizePage)
        self.optimizerButton.setObjectName(u"optimizerButton")
        self.optimizerButton.setMinimumSize(QSize(0, 40))
        self.optimizerButton.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.optimizerButton, 2, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.paretoPlot = QWebEngineView(optimizePage)
        self.paretoPlot.setObjectName(u"paretoPlot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.paretoPlot.sizePolicy().hasHeightForWidth())
        self.paretoPlot.setSizePolicy(sizePolicy2)
        self.paretoPlot.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.paretoPlot, 3, 2, 1, 2)

        self.optimizeResultTable = TableWidget(optimizePage)
        self.optimizeResultTable.setObjectName(u"optimizeResultTable")
        sizePolicy2.setHeightForWidth(self.optimizeResultTable.sizePolicy().hasHeightForWidth())
        self.optimizeResultTable.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.optimizeResultTable, 0, 0, 4, 1)


        self.retranslateUi(optimizePage)

        QMetaObject.connectSlotsByName(optimizePage)
    # setupUi

    def retranslateUi(self, optimizePage):
        optimizePage.setWindowTitle(QCoreApplication.translate("optimizePage", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("optimizePage", u"\u79cd\u7fa4\u6570\u91cf", None))
        self.label.setText(QCoreApplication.translate("optimizePage", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.optimizerButton.setText(QCoreApplication.translate("optimizePage", u"\u5f00\u59cb\u4f18\u5316", None))
    # retranslateUi

