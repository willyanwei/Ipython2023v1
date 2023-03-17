# -*- coding: utf-8 -*-
# @Time    : 2023/3/17 10:03
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : jd_report.py
# @Software: PyCharm

from IRAHO.EasyReportCode.easy.base.DbHelper import *
# DB_Info.ini配置文件所在位置
db_info_file = r"E:\Ipython\IRAHO\EasyReportCode\easy\base\DB_info.ini"


sql = 'show databases;'
qd = QueryDB().queryMysqlDB('MYSQL', sql, db_info_file)
print(qd)
