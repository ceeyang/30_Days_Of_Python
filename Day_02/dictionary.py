#!/usr/bin/env python3
# -*- coding:utf-8 -*-

d = {'bob':90,'cee':100,'lee':99}
print(d)
print(d['bob']) # 根据 key 取值

d['yang'] = 80  # 根据 key 赋值
print(d['yang'])

# 如果 key 不存在，则会报错，字典有两种方法判断 key 是否存在：
# 第一种：in
if 'yang' in d:
    print("'yang' is a key for d")
else:
    print("'yang' is not a key for d")
# 第二种：
lee  = d.get('lee')   # key 存在，则返回对应的 value
jack = d.get('jack')  # key 不存在，则返回 None
print(lee)
print(jack)


# 删除一个 key ，用 pop(key)方法，对应的 value 也会从 dict 中删除
d.pop('lee')
print(d)
