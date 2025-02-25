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



def edge():
    cap_1 = cv2.imread(path_input_data+"/origin_1.jpg",cv2.IMREAD_COLOR)
    cap_2 = cv2.imread(path_input_data+"/origin_2.jpg",cv2.IMREAD_COLOR)
    cap_list = [cap_1,cap_2]
    cap_1 = cv2.imread(path_input_data+"/origin_stop.jpg",cv2.IMREAD_COLOR)
    cap_2 = cv2.imread(path_input_data+"/origin_stop.jpg",cv2.IMREAD_COLOR)
    cap_list = [cap_1,cap_2]
    counter = 0
    for c in cap_list:
        counter += 1
        # _, frame = c.read()
        hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0,0,160])
        upper_white = np.array([255,255,255])
        mask = cv2.inRange(hsv, lower_white, upper_white)
        # gray = cv2.cvtColor(c, cv2.COLOR_RGB2GRAY)
        # kernel_size = 3
        # blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)
        # blur_edges = cv2.Canny(blur_gray,20,30)
        # cv2.imshow('blur_Edges',blur_edges)
        # cv2.imwrite(path_output_data+"/blur_edges_%d.jpg"%(counter), blur_edges)
        cv2.imwrite(path_output_data+"/stopmask_%d.jpg"%(counter), mask)

if __name__ == '__main__':
    edge()
    cv2.destroyAllWindows()
    # cap.release()