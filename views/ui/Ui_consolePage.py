# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consolePage.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_consolePage(object):
    def setupUi(self, consolePage):
        if not consolePage.objectName():
            consolePage.setObjectName(u"consolePage")
        consolePage.resize(1420, 915)
        self.horizontalLayout = QHBoxLayout(consolePage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.console = QTextBrowser(consolePage)
        self.console.setObjectName(u"console")

        self.horizontalLayout.addWidget(self.console)


        self.retranslateUi(consolePage)

        QMetaObject.connectSlotsByName(consolePage)
    # setupUi

    def retranslateUi(self, consolePage):
        consolePage.setWindowTitle(QCoreApplication.translate("consolePage", u"Form", None))
    # retranslateUi

