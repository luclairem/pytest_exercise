# -*- coding:utf-8 -*-
# Time : 2022/4/4 21:01
# Author : Lu
# File : config.py
# Desc :

import os

root_path = os.path.dirname(os.path.dirname(__file__))
# print("ddddd",root_path)
# root_path = D:\Users\lu\PycharmProjects\pythonProject\WebTesting\4_3_pytest

url = 'http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html'
driver_path = r'F:\edgedriver_win64\msedgedriver.exe'

case_path = root_path+r'/testcases'
file_path = root_path+r'/data/test.xlsx'
system_version = '1.1'
log_file = root_path+r'/log/log.txt'



