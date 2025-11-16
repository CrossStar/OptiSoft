'''
Author: Zhixin Wu && wuzhixin.321@qq.com
Date: 2025-03-01 15:51:18
LastEditTime: 2025-03-02 19:08:11

Copyright (c) 2025 by wuzhixin.321@qq.com, All Rights Reserved. 
'''

from enum import Enum
from qfluentwidgets import FluentIconBase, getIconColor, Theme

class Icon(FluentIconBase, Enum):
    CONSOLE = "console"
    LINK = "link_square"
    CODE = "code"
    TRENDING = "trending"
    def path(self, theme=Theme.AUTO):
        return f":/resource/icons/{self.value}.svg"
