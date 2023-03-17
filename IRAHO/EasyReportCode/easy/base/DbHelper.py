# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 15:31
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : DbHelper.py
# @Software: PyCharm

import os
import configparser
import pandas as pd
# from pyhive import hive
import pymysql


# DB_info信息
class DBInfo():
    def __init__(self, dbtype, host, dbport, dbuser, dbpassword, dbname):
        # 在_init_ 方法内部使用 self 属性名 = 属性的初始值 就可以 定义属性；
        # 定义属性之后，再使用 Cat 类创建的对象，都会拥有该属性
        # print("数据库配置信息如下：")
        self.dbtype = dbtype
        self.host = host
        self.dbport = dbport
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbname = dbname


# 获取DBInfo
class GetDBInfo():
    def getMysqlDBInfo(self, Dsn, db_info_file):
        db_config = configparser.ConfigParser()
        db_config.read(db_info_file)
        di = DBInfo(db_config[Dsn]['dbtype'],
                    db_config[Dsn]['host'],
                    db_config[Dsn]['dbport'],
                    db_config[Dsn]['dbuser'],
                    db_config[Dsn]['dbpassword'],
                    db_config[Dsn]['dbname'])
        return di


class QueryDB():
    def queryMysqlDB(self, Dsn, Sql, db_info_file):
        di = GetDBInfo().getMysqlDBInfo(Dsn, db_info_file)
        connection = pymysql.connect(user=di.dbuser,
                                     password=di.dbpassword,
                                     host=di.host,
                                     database=di.dbname,
                                     port=int(di.dbport))
        cur = connection.cursor()
        cur.execute(Sql)
        data = list(cur.fetchall())
        col_name_list = [tuple[0] for tuple in cur.description]
        df = pd.DataFrame(data, columns=col_name_list)
        connection.commit()
        connection.close()
        return df

    def queryError(self, di, Sql):
        """如果数据库的类型在DB_info.ini配置中找不到，则抛出异常"""
        raise Exception("未定义" + di.dbtype + "类型数据库的查询方法...")

    def __call__(self, Dsn, Sql, db_info_file):
        di = GetDBInfo(Dsn, db_info_file)
        switcher = {'SQLITE': self.queryMysqlDB()}
        print(f"swotcher输出为：{switcher}")
        # func = switcher.get(di.dbtype.upper(), lambda x, y: self.queryError(di, Sql))

# """尝试登录MYSQL并查询数据"""
# sql = "show databases;"
# qd = QueryDB().queryMysqlDB("MYSQL", sql)
# print(qd)

# class CommitDB():
#     def commitMysqlDB(self, Dsn, Sql):
#         di = GetDBInfo().getMysqlDBInfo(Dsn)
#         connection = pymysql.connect(user= di.dbuser,
#                                      password=di.dbpassword,
#                                      host=di.host,
#                                      database=di.dbname,
#                                      port=int(di.dbport))
#         cur = connection.cursor()
#         cur.execute(Sql)
#         cur.execute('commit')
#         connection.close()
#         print("commit成功")
# #
# sql = "CREATE database if not exists jd_db_new;"
# cd = CommitDB().commitMysqlDB("MYSQL", sql)
