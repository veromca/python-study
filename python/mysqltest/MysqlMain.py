#!/usr/bin/python
from python.mysqltest.MysqlTest import MysqlTest
from python.mysqltest.pyMysql import pyMysql

"""
mysql CURD 测试
"""

def mysqlConnector():
    mysqlTest = MysqlTest()
    databases = mysqlTest.getAllDataBases()
    for x in databases:
        print(x)
    # createTable(mydb)
    print('*********getAllTables**********')
    tables = mysqlTest.getAllTables()
    for table in tables:
        print(table)
    print('*********insert**********')
    mysqlTest.insert('紫色', '128G')
    print('*********select ALL**********')
    rows = mysqlTest.selectAll()
    for row in rows:
        print(row)
    print('*********get One**********')
    oneRow = mysqlTest.getOne('1')
    print(oneRow)
    print('*********update**********')
    updateCount = mysqlTest.update('1', '银色', '256G')
    print(updateCount)

def pyMysqlTest():
    pymysql = pyMysql()
    pymysql.saveReptile('黄色','256')
    rows = pymysql.selectAll()
    print('*********select ALL size: %s **********',len(rows))

if __name__ == "__main__":
    # mysqlConnector()
    pyMysqlTest()
