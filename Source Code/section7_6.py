# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2022 BJTU Academic Support Centre. All Rights Reserved
#
################################################################################

def fun(*zzz):  # zzz 为参数名称
    print(zzz)


fun(10)
fun(10, 99)
fun(56, 45, 78)


def fun(**zzz):
    print(zzz)


fun(a=52)
fun(a=56, b=111)


def fun2(*zzz, **yyy):
    pass
