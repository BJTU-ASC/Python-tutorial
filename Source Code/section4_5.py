# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2022 BJTU Academic Support Centre. All Rights Reserved
#
################################################################################

import math
radius = eval(input("Enter a number:"))

if radius >= 0:
    area = radius * radius * math.pi
    print("The area for the circle of radius", radius, "is", area)


i = eval(input("i="))
j = eval(input("j="))
k = eval(input("k="))

if i > j:
    if i > k:
        print('A')
else:
    print('B')


i = eval(input("i="))
j = eval(input("j="))
k = eval(input("k="))

if i > j:
    if i > k:
        print('A')
else:
    print('B')
