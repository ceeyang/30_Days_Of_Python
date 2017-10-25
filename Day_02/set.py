#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。

# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print(s)

# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
# 显示的顺序也不表示set是有序的,重复元素在set中自动被过滤：
s = set([1,2,3,2,3,4,5,0])
print(s)


s.add(9) # 通过 add(key) 可以添加元素到 set 中，重复添加只会添加一个。
print(s)

s.remove(9) # 通过 remove(key) 可以删除元素
print(s)


# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s_one = set([1,2,3,4])
s_two = set([2,3,4,5])
s = s_one & s_two
print(s)
s = s_one | s_two
print(s)


a = ['c','b','a','d']
a.sort()
print(a)

a = 'abc'
a.replace('a','A')
print(a)
