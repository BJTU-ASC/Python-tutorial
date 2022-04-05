# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2022 BJTU Academic Support Centre. All Rights Reserved
#
################################################################################

def fun(a, b=10):
    print(a, b)  # 函数的调用


fun(100)  # 只传一个参数100给a，b采用默认值10。
fun(20, 30)


def cal(a, b=10):
    sum = a + b
    return sum


ret = cal(3)
print(ret)
