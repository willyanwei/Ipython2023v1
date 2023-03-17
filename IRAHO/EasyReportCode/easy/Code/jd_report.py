# -*- coding: utf-8 -*-
# @Time    : 2023/3/17 10:03
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : jd_report.py
# @Software: PyCharm

from IRAHO.EasyReportCode.easy.base.DbHelper import *

sql = 'show databases;'
qd = QueryDB().queryMysqlDB('MYSQL',  sql)
print(qd)
