import pymongo
"""
python 操作 mongo
"""

# 创建数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# 判断数据库是否已存在
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
print(dblist)
if "runoobdb" in dblist:
  print("数据库已存在！")

