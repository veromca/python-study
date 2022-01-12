#!/usr/bin/python
"""
mysql.connector 连接Mysql数据库并进行CRUD
"""

import mysql.connector
from pydantic import BaseModel

class ReptileEntity(BaseModel):
    global product_color
    global product_size
    def __init__(self, color, size):
        self.product_color = color
        self.product_size = size

class MysqlTest:
    def __init__(self):
        mydbs = mysql.connector.connect(
            host="127.0.0.1",  # 数据库主机地址
            user="test_user",  # 数据库用户名
            passwd="test",  # 数据库密码
            database="test_db"  # 数据库
        )
        global mydb
        global mycursor
        self.mydb = mydbs
        self.mycursor = mydbs.cursor()

    def getAllDataBases(self):
        self.mycursor.execute("SHOW DATABASES")
        return self.mycursor

    def getAllTables(self):
        self.mycursor.execute("SHOW TABLES")
        return self.mycursor

    def createTable(self):
        self.mycursor.execute("CREATE TABLE test_reptile (product_color VARCHAR(255), product_size VARCHAR(255))")
        return self.mycursor

    def insert(self,param: ReptileEntity):
        sql = "INSERT INTO test_reptile (product_color, product_size) VALUES (%s, %s)"
        val = (param.product_color, param.product_size)
        #self.mycursor.execute(sql, val)
        #self.mydb.commit()  # 数据表内容有更新，必须使用到该语句
        #print(self.mycursor.rowcount, "记录插入成功。")
        print(param.product_color,param.product_size,"记录插入成功。")

    def selectAll(self):
        sql = "select * from test_reptile"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        return result

    def getOne(self,id):
        sql = "select * from test_reptile where id = %s"
        param = (id,)
        self.mycursor.execute(sql, param)
        result = self.mycursor.fetchone()
        return result

    def update(self,id, product_color, product_size):
        sql = "update test_reptile set product_color = %s,product_size= %s where id = %s"
        param = (product_color, product_size, id)
        self.mycursor.execute(sql, param)
        self.mydb.commit()  # 数据表内容有更新，必须使用到该语句
        print(self.mycursor.rowcount, " 条记录被修改")
        return self.mycursor.rowcount