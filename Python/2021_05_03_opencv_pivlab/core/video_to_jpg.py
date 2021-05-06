#-*- coding: utf-8 -*-
u'''
        Author          : 蔡易展
        Date            : 2021/05/06
        Version         : 0.0.0.1
        Description     : Hsu_project
'''

# standard module
import os
import sys
CWD = os.path.dirname(os.path.dirname(__file__))
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
import cv2
import numpy as np

# local module
import config as config

def read_video():
    cap = cv2.VideoCapture(config.INPUT_VIDEO_PATH)
    counter = 0
    _, frame = cap.read()
    while(type(frame) is np.ndarray):
        counter += 1
        print("Output " + config.VTJ_JPG_PATH + "/origin_%d.jpg"%(counter))
        cv2.imwrite(config.VTJ_JPG_PATH + "/origin_%d.jpg"%(counter), frame)
        _, frame = cap.read()
    cap.release()