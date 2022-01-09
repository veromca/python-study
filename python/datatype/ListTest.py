#!/usr/bin/python
"""
List
"""
list = ['zhangsan',1990,'lisi',1989]
tinylist = ['runoob',1988]
print(list)
print(list[0])
print(list[2:])
print(tinylist*2)
print(list + tinylist)

list.pop(2)
list.append('wangwu')
print(list)

def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

"""
tuple
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
"""
tuple = ('zhaoliu',1992,list)
print(tuple)
list2 = [tuple,list]
print(list2)

"""
Set
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu','Runoob'}
# 输出集合，重复的元素'Runoob'被自动去掉
print(sites)
sites.add('wangyi')
sites.update({'xl','tx'})
print(sites)
print(len(sites))
# 成员测试
if 'wangyi' in sites:
    print("wangyi 在集合sites中")
else:
    print("wangyi 不在集合sites中")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

"""
Dictionary 字典
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
"""
dict1 = {}
dict1['key1'] = "Hello,Python!"
dict1[2] = "Hello,Java!"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(dict1['key1'])
print(dict1[2])
print(dict1.keys())
print(tinydict.values())

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
testdict = dict([('name','lisi'),('code',2),('work','taobao')])
print(testdict)