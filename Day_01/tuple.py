#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# tuple 不可变的有序列元组,没有 append() 和 insert()方法。
# tuple 不可变，使代码更安全。如果可能，能用 tuple 就用 tuple
classmates = ("bob","tony","cee","lee")
print("classmates =",classmates)


# 如果定义一个空的 tuple,可以写成（）
t = ()
print(t)


# 只有一个元素的tuple,由于()既可以表示tuple，又可以表示数学公式中的小括号
# 只有一个元素的 tuple 必须在后面加上一个逗号‘,’，来消除歧义。
singleTuple = (1,)
print(singleTuple)


# 当tuple 里的其中元素是 list 时，list 里面的内容可以改变。
# list 里面的内容变了，但 tuple 指向 list 的地址并没有变
t = ('a','b','c',['d','e','f'])
print(t)
t[3][0] = "g"
t[-1][1] = "h"
t[-1][-1] = "i"
print(t)




