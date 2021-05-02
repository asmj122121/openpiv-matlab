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

# local module

# import config as config


if __name__ == '__main__':
    print("hello world")