#-*- coding: utf-8 -*-
u'''
        Author          : 蔡易展
        Date            : 2021/04/12
        Version         : 0.0.0.1
        Description     : web crawler

        version         : 0.0.0.1
'''

# standard module
import os
import sys
CWD = os.path.dirname(__file__)
path_core = os.path.join(CWD, 'core')
path_ui = os.path.join(CWD, 'ui')
path_settings = os.path.join(CWD, 'settings\\default')
path_3rd_module = os.path.join(CWD, '3rd_module')
p_list = [
            path_core,
            path_ui,
            path_settings,
            path_3rd_module
]
for p in p_list:
    if p not in sys.path:
        sys.path.insert(0, p)

# 3rd module
try:
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2.QtWidgets import *
    from PySide2 import __version__
except ImportError:
    from PySide import QtCore
    from PySide.QtCore import Qt
    from PySide import QtGui
    from PySide.QtGui import *
    from PySide import __version__

# local module



if os.environ.has_key('CHEER_TD_TEST'):
    reload(srt_core)

class Calendar(QWidget):
    cal_signal = QtCore.Signal(str)
    def __init__(self,x,y):
        super(Calendar, self).__init__()
        self.init_UI()
        self.setGeometry(x,y,250,160)
    def init_UI(self):
        self.cal = QCalendarWidget(self)
        self.cal.clicked[QtCore.QDate].connect(self.cal_method)
    def cal_method(self,date):
        date_str = date.toString('yyyy / MM / dd')
        self.cal_signal.emit(date_str)