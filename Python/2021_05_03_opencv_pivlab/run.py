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
print(path_core)
# 3rd module

# local module
import video_to_jpg as vtj
import RGB_to_Edge as rte
import config

if __name__ == '__main__':
    vtj.read_video()
    # rte.edge()