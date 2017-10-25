#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# python 的 for 循环分为两种：
# 第一种：for...in 循环
names = ['Bob','cee','lee']
for name in names:
    print(name)


# for x in ... 循环就是把每个元素带入变量 x,然后执行缩进块语句
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += sum + x
print(sum)


# range() 函数可以生产一个整数序列
# list() 函数可以转化为 list。
a = list(range(5))
print(a)
sum = 0
for x in list(range(101)):
    sum += x
print(sum)


# 第二种循环是 while 循环
sum = 0
n = 100
while n>0:
    sum = sum+n
    n = n-1
print(sum)


# break 可以提前终止循环
# continue 跳过当次循环，直接开始下一轮循环
sum = 0
n = 100
while n>0:
    n = n - 1
    if n < 90:     # 当 n 小于等于90
        break      # break 提前退出整个循环
    if n % 2 == 0: # 如果 n 是偶数，执行 continue 语句
        continue   # continue 语句会直接继续下一轮循环，后续 print并不会执行
    print(n)
