# -*- coding:utf-8 -*-
# Time : 2022/4/5 16:06
# Author : Lu
# File : log.py
# Desc :

import logging
from config.config import log_file

# 创建日志器
loggers = logging.getLogger()
# 定义日志器的级别
loggers.setLevel(logging.INFO)
# 定义处理器的格式
formatF = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
# 创建处理器
logfile = log_file
fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
# 设置处理器的级别
fh.setLevel(logging.INFO)
# 设置处理器的格式
fh.setFormatter(formatF)
# 添加至日志器
loggers.addHandler(fh)




