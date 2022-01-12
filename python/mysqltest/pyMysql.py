#!/usr/bin/python

import pymysql
"""
PyMysql 连接Mysql数据库并进行CRUD
"""

class pyMysql:
    def __init__(self):
        mydbs = pymysql.connect(
            host="127.0.0.1",  # 数据库主机地址
            user="test_user",  # 数据库用户名
            passwd="test",  # 数据库密码
            database="test_db"  # 数据库
        )
        global mydb
        global mycursor
        self.mydb = mydbs
        self.mycursor = mydbs.cursor()

    def createTable(self):
        try:
            # 使用 execute() 方法执行 SQL，如果表存在则删除
            self.mycursor.execute("DROP TABLE IF EXISTS test_reptile")

            # 使用预处理语句创建表
            sql = """CREATE TABLE test_reptile (
            id INT PRIMARY KEY AUTO_INCREMENT,
            product_color VARCHAR(255), 
            product_size VARCHAR(255))
            """
            self.mycursor.execute(sql)
        except:
            print('create table test_reptile fail')
        finally:
            print('create table test_reptile success')
            # 关闭数据库连接
            # self.mydb.close()

    def saveReptile(self,product_color,product_size):
        # SQL 插入语句
        sql = "INSERT INTO test_reptile (product_color, product_size) VALUES (%s, %s)"
        val = (product_color, product_size)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()  # 数据表内容有更新，必须使用到该语句
            print(self.mycursor.rowcount, "记录插入成功。")
        except:
            # 如果发生错误则回滚
            self.mydb.rollback()
        # 关闭数据库连接
        # self.mydb.close()

    def selectAll(self):
        # SQL 查询语句
        sql = "SELECT * FROM test_reptile \
               WHERE id > %s" % (1)
        try:
            # 执行SQL语句
            self.mycursor.execute(sql)
            # 获取所有记录列表
            results = self.mycursor.fetchall()
            for row in results:
                color = row[0]
                size = row[1]
                id = row[2]
                # 打印结果
                print("color=%s,size=%s,id=%s" % \
                      (color, size, id))
            return results
        except:
            print("Error: unable to fetch data")