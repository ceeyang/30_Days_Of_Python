#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

# 自定义一个求绝对值的函数，并添加参数类型判断
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x = move(100, 200, 80, math.pi/6)
print(x)
x, y = move(100, 200, 80, math.pi/6)
print(x, y)


# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000
# 上面页面的练习题，暂没做出来。
def quadratic(a, b, c):
    if not isinstance(a, (int, float), b, (int, float), c, (int, float)):
        raise TypeError('bad operand type')
    pass



# 对于多个参数的函数，可以设置默认值。
# 设置默认值后，不会影响原有的只有一个参数的函数调用
# 例如：对一个数求n次方，默认2次方
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2))
print(power(2,3))


# 当参数过多时，其他没有设置默认值的参数可以不依次传入
# 设置过默认值得可以不传，也可以指定某一个值传入：
def enroll(name, gender, age=6, city='ShenZhen'):
    print(name)
    print(gender)
    print(age)
    print(city)

enroll('cee','M')
enroll('cee','M',23)
enroll('cee','M',city='SiChuan')


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2)
nums = [1, 2, 3, 4, 5, 6, 7]
calc(*nums)


# **kw 关键字
# 函数person除了必选参数name和age外，还接受关键字参数kw。
# 在调用该函数时，可以只传入必选参数
# 也可以传入任意个数的关键字参数
# ** 关键字 传入该 list 的每个元素
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


person('cee', 23, city='ShenZhen')
person('lee', 24, gender='M', city='ChengDu')
info = {'gender':'M', 'job':'iOS Developer', 'City':'ShenZhen'}
person('jony', 23, **info)


# 命名关键字参数
# 要限制关键字参数的名字，就可以用命名关键字参数，
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def people(name, age, *, city, job):
    print(name, age, city, job)



# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# NOTE: *args 是可变参数，args接收的是一个tuple；
# NOTE: **kw 是关键字参数，kw接收的是一个dict
# NOTE: 没有设置默认参数的必传。
# NOTE: 默认参数必须是一个不可变的对象
