'''
Author: Zhixin Wu && wuzhixin.321@qq.com
Date: 2025-03-01 15:51:16
LastEditTime: 2025-03-01 16:00:40

Copyright (c) 2025 by wuzhixin.321@qq.com, All Rights Reserved. 
'''

import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from views.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    window.setMicaEffectEnabled(False)

    sys.exit(app.exec())