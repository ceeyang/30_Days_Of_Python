#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建一个 list, 可变的数组，类似于ios 的可变数组
classmates = ["Bob","cee","yang","lee"]
print("classmates = ",classmates)

# len() 获取当前 list 的长度 
print("len(classmates) = ",len(classmates))

# list[index] 根据下标获取对应的值，index 值前面加上‘-’号表示倒数第几个值
print("classmates[0] = ",classmates[0])
print("classmate[-1] = ",classmates[-1])

# append():  list 里面末尾添加元素
# insert(index,XX) : list 某一个插入某一个元素到具体下标位置
classmates.append("Last")
print("classmates.append('Last') = ",classmates)
classmates.insert(1,"tony")
print("classmates.insert(1,'tony') =",classmates)

# pop() 删除末尾元素，括号里面出入 index 值，删除具体某一个元素
classmates.pop()
print("classmates.pop() =",classmates)
classmates.pop(1)

