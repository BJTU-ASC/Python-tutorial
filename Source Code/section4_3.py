# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2022 BJTU Academic Support Centre. All Rights Reserved
#
################################################################################

a = 0
if a > 1:
    print("当a大于1时这句话将会被输出")
else:
    print("当a小于1时这句话将会被输出")


import math
radius = eval(input("Enter a number:"))

if radius >= 0:
    area = radius * radius * math.pi
    print("The area for the circle of radius", radius, "is", area)
else:
    print("Negative input")


number = eval(input("Enter an integer:"))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
