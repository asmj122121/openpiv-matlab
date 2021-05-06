#-*- coding: utf-8 -*-
u'''
        Author          : 蔡易展
        Date            : 2021/04/12
        Version         : 0.0.0.1
        Description     : Hsu_project
'''

# standard module
import os
import sys
CWD = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_core = os.path.join(CWD, 'core')
path_ui = os.path.join(CWD, 'ui')
path_settings = os.path.join(CWD, 'settings\\default')
path_3rd_module = os.path.join(CWD, '3rd_module')
path_input_data = os.path.join(CWD, 'input_data')
path_output_data = os.path.join(CWD, 'output_data')
p_list = [
            path_core,
            path_ui,
            path_settings,
            path_input_data,
            path_3rd_module
]
for p in p_list:
    if p not in sys.path:
        sys.path.insert(0, p)

# 3rd module

# local module

VERSION = '0.0.0.1'

#_____ui_____
MAIN_UI_WIDTH  = 500
MAIN_UI_HEIGHT = 160

#_____RGB_to_Edge_____
INPUT_VIDEO_NAME = "/20210503_1.mp4"
INPUT_VIDEO_PATH = path_input_data+INPUT_VIDEO_NAME
VTJ_JPG_PATH = path_input_data