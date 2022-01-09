#!/usr/bin/python
"""
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
"""
def fseries(limit):
    list = []
    a,b = 0,1
    while b < limit:
        list.append(b)
        a,b = b,a+b
    else:
        print('超过最大限制:'+str(b))
    return list

if __name__ == "__main__":
    input = 500
    resp = fseries(input)
    print(resp)