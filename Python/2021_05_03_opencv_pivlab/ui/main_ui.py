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
import crawler as crawler
import sub_ui as sub_ui
import config as config

if os.environ.has_key('CHEER_TD_TEST'):
    reload(srt_core)



class SampleWidget(QMainWindow):
    def __init__(self, parent=None):
        '''
            [in] parent     :  str, parent object name
        '''
        super(SampleWidget, self).__init__(parent=parent)
        self.resize(config.MAIN_UI_WIDTH, config.MAIN_UI_HEIGHT)
        self.init_widget()
        self.init_layout()
        self.init_connection()

    def init_widget(self):
        self.init_groupbox_cal()
    
    def init_groupbox_cal(self):
        self.ui_groupbox_cal = QGroupBox()
        layout = QGridLayout()

        label_start = QLabel('START Date:')
        self.ui_edt_start = QLineEdit()
        label_end   = QLabel('END Date:')
        self.ui_edt_end   = QLineEdit()
        label_pos   = QLabel('Data  Pos :')
        self.ui_edt_pos   = QLineEdit()
        self.ui_btn_start = QPushButton('Calender')
        self.ui_btn_end   = QPushButton('Calender')
        self.ui_btn_fold  = QPushButton('Select Folder')
        self.ui_btn_get   = QPushButton('Get excel')
        layout.addWidget(label_start, 0, 0)
        layout.addWidget(self.ui_edt_start, 0, 1)
        layout.addWidget(self.ui_btn_start, 0, 2)
        layout.addWidget(label_end, 0, 3)
        layout.addWidget(self.ui_edt_end, 0, 4)
        layout.addWidget(self.ui_btn_end, 0, 5)
        layout.addWidget(label_pos, 1, 0)
        layout.addWidget(self.ui_edt_pos, 1,1,1,3)
        layout.addWidget(self.ui_btn_fold, 1, 4)
        layout.addWidget(self.ui_btn_get, 1, 5)
        # self.ui_edt_start.setText("")
        # self.ui_edt_end.setText("")
        self.ui_groupbox_cal.setLayout(layout)

    def init_layout(self):
        lay = QVBoxLayout()
        lay.addWidget(self.ui_groupbox_cal)

        w = QWidget()
        self.setCentralWidget(w)
        w.setLayout(lay)

    def init_connection(self):
        self.ui_btn_start.clicked.connect(self.calender_start_method)
        self.ui_btn_end.clicked.connect(self.calender_end_method)
        self.ui_btn_fold.clicked.connect(self.folder_method)
        self.ui_btn_get.clicked.connect(self.get_xlsx_method)

    def emit_start_method(self, date_str):
        self.ui_edt_start.setText(date_str)
        register_list = date_str.split(' / ')
        config.START_YEAR_INT  = int(register_list[0])
        config.START_MONTH_INT = int(register_list[1])
        config.START_DATE_INT  = int(register_list[2])
    def calender_start_method(self):
        self.sub_window = sub_ui.Calendar(self.geometry().x()+config.MAIN_UI_WIDTH+5, self.geometry().y())
        self.sub_window.cal_signal.connect(self.emit_start_method)
        self.sub_window.show()

    def emit_end_method(self, date_str):
        self.ui_edt_end.setText(date_str)
        register_list = date_str.split(' / ')
        config.END_YEAR_INT  = int(register_list[0])
        config.END_MONTH_INT = int(register_list[1])
        config.END_DATE_INT  = int(register_list[2])
    def calender_end_method(self):
        self.sub_window = sub_ui.Calendar(self.geometry().x()+config.MAIN_UI_WIDTH+5, self.geometry().y())
        self.sub_window.cal_signal.connect(self.emit_end_method)
        self.sub_window.show()

    def folder_method(self):
        position = QtGui.QFileDialog.getExistingDirectory()
        config.update()
        config.TARGET_POS = os.path.join( position, config.XLSX_NAME)
        self.ui_edt_pos.setText(config.TARGET_POS)

    def get_xlsx_method(self):
        crawler.run()

    def closeEvent(self, event):
        sys.exit(0)
        pass



def run():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("plastique"))

    window = SampleWidget()
    window.setWindowTitle('Find late people v%s' % config.VERSION)
    window.show()

    sys.exit(app.exec_())