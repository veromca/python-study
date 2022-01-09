#!/usr/bin/python
"""
For循环
Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""
languages = ['C','C++','Perl','Python','Java']
for x in languages:
    if x == 'Python':
        print('Python,跳出循环！')
        continue
    else:
        print(x)
else:
    print("没有循环数据")

"""
range()函数
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，
"""
print('---------------')
for i in range(len(languages)):
    print(i,languages[i])
