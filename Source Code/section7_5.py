# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2022 BJTU Academic Support Centre. All Rights Reserved
#
################################################################################

def cal(a, b):  # a,b称为形式参数，形参的位置是在函数的定义处
    # a,b在括号里没有具体的值
    sum = a + b
    return sum


sum = cal(10, 15)  # 10,15称为实际参数的值，实参的位置也是函数的调用处
print(sum)


def cale(a, b):
    c = a + b
    return c


ret = cale(b=77, a=99)  # = 左侧的变量名称称为 关键字参数
print(ret)
