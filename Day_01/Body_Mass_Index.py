#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("根据用户输入身高体重，计算用户BMI 指数。")
print("BMI 公式：体重除以身高的平方")

height = input("Please enter your height(m): ")
weight = input("Please enter your weight(kg): ")
height = float(height)
weight = float(weight)
bmi = weight / (height * height)
print("您的BMI指数为：",bmi)
if bmi < 18.5:
    print("过轻")
elif bmi > 18.5 and bmi < 25:
    print("正常")
elif bmi > 25 and bmi < 28:
    print("过重")
elif bmi > 28 and bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
