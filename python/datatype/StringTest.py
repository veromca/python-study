#!/usr/bin/python
# 导入 sys 模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# 导入特定的成员
from sys import argv, path

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以有多行组成。。。
"""
print(paragraph)
str = "123456789"
# 输出第一个到倒数第二个的所有字符
print(str[0:-1])
print(str[2])
print(str[2:])
# 输出字符串3次
print(str*3)
print(str +' Hello,Python!')
# 使用反斜杠(\)+n转义特殊字符
print('hello\nPython!')
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print(r'hello\nPython!')

#Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 以下代码中 ，\n\n 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。
# input("\n\n按下 enter 键后退出。")

a = 1
b = 2
if a==1:
    print('OK')
else:
    print('Fail')