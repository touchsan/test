#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "Safeepay123", "pythondb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
     FIRST_NAME CHAR(30) NOT NULL,
     LAST_NAME CHAR(28),
     AGE INT(12),
     SEX CHAR(5),
     YEAR INT (33),
     INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()