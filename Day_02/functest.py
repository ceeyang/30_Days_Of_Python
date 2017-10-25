#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x



# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
