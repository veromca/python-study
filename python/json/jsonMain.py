#!/usr/bin/python3
"""
Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。

Python 编码为 JSON 类型转换对应表：
Python	JSON
dict	object
list, tuple	array
str	string
int, float, int- & float-derived Enums	number
True	true
False	false
None	null
JSON 解码为 Python 类型转换对应表：
JSON	Python
object	dict
array	list
string	str
number (int)	int
number (real)	float
true	True
false	False
null	None
"""

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'python',
    'url': 'http://www.python.com'
}

jsonObj = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 字符串：", jsonObj)


jsonObj2 = json.loads(jsonObj)
print ("JSON 对象：", jsonObj)
print("JsonObj name:",jsonObj2['name'])

"""
如果你要处理的是文件而不是字符串，你可以使用
json.dump()
和
json.load()
来编码和解码JSON数据。例如：
"""
# 写入 JSON 数据
with open('mydata.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('mydata.json', 'r') as f:
    data = json.load(f)