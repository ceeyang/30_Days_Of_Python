#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 缩进规则：4个空格
a = 100
if a > 100:
    print(a)
else:
    print(-a)


# elif 是 else if 的缩写。
a = 24
if a < 1:
    print("Baby")
elif a < 18:
    print("Teenagers")
elif a < 35:
    print("Man")
else:
    print("Old man")


# 条件判断的简化，如果 a 存在，就执行下面的语句
if a:
    print(a)


# input 输入的内容为字符串，需要根据相关函数转换。此处用 int()函数转换为 int 类型
birth = input('birth: ')
if int(birth) > 2000:
    print("00后")
else:
    print("00前")




