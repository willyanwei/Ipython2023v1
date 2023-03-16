# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 16:56
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : tmp.py
# @Software: PyCharm

import os
import configparser
# import pandas as pd
# from pyhive import hive
import pymysql


# class DBInfo():
#     def __init__(self, dbtype, host, dbport, dbuser, dbpassword, dbname):
#         # 在_init_ 方法内部使用 self 属性名 = 属性的初始值 就可以 定义属性；
#         # 定义属性之后，再使用 Cat 类创建的对象，都会拥有该属性
#         print("数据库配置信息如下：")
#         self.dbtype = dbtype
#         self.host = host
#         self.dbport = dbport
#         self.dbuser = dbuser
#         self.dbpassword = dbpassword
#         self.dbname = dbname
# DB_Info.ini配置文件所在位置
db_info_path = "DB_info.ini"

db_config = configparser.ConfigParser()
db_config.read(db_info_path)

print(db_config['MYSQL']['dbtype'])


# di = DBInfo(db_config[a]['dytype'],
#             db_config[a]['host'],
#             db_config[a]['dbport'],
#             db_config[a]['dbuser'],
#             db_config[a]['dbpassword'],
#             db_config[a]['dbname'])