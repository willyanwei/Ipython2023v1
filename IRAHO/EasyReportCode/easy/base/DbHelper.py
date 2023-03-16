# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 15:31
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : DbHelper.py
# @Software: PyCharm

import os
import configparser
# import pandas as pd
# from pyhive import hive
import pymysql

# DB_Info.ini配置文件所在位置
db_info_path = "DB_info.ini"

# 获取DB_info信息
class DBInfo():
    def __init__(self, dbtype, host, dbport, dbuser, dbpassword, dbname):
        # 在_init_ 方法内部使用 self 属性名 = 属性的初始值 就可以 定义属性；
        # 定义属性之后，再使用 Cat 类创建的对象，都会拥有该属性
        print("数据库配置信息如下：")
        self.dbtype = dbtype
        self.host = host
        self.dbport = dbport
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbname = dbname



class GetDBInfo():
    def getMysqlDBInfo(self, Dsn, isdec = False):
        db_config = configparser.ConfigParser()
        db_config.read(db_info_path)
        di = DBInfo(db_config[Dsn]['dbtype'],
                    db_config[Dsn]['host'],
                    db_config[Dsn]['dbport'],
                    db_config[Dsn]['dbuser'],
                    db_config[Dsn]['dbpassword'],
                    db_config[Dsn]['dbname'])
        return di


class QueryDB():
    def queryMysqlDB(self, di, Sql):
        connection = pymysql.connect(user= di.dbuser,
                                     password=di.dbpassword,
                                     host=di.host,
                                     database=di.dbname,
                                     port=int(di.dbport))
        cur = connection.cursor()
        cur.execute(Sql)


# #  根据DB_Info查询数据
# class QueryDB():
#     def queryHive(self, di, Sql):
#