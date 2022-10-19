#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:28:07 2022

@author: muzian
"""

from function_database import *

# Mode Choose
mode = int(input("请选择运行模式：1.手动输入模式； 2.通过账号自动获取模式 -->"))

mod_choose(mode)

year = float(input("请输入您现在所在的年级，如为半学期可选择为0.5，如：大一上，则输入0.5；大一下，则输入1；以此类推。-->"))

if year == 0.5:
    print("Pass")
    year_0_5()
elif year == 1.0:
    print("Pass")
elif year == 1.5:
    print("Pass")
elif year == 2.0:
    print("Pass")
elif year == 2.5:
    print("Pass")
elif year == 3.0:
    print("Pass")
elif year == 3.5:
    print("Pass")
elif year == 4.0:
    print("Pass")
elif year <= 0:
    print("你还没上学呢，算什么算")
elif year >= 4.0:
    print("你已经毕业了，只能按你毕业时的成绩算哦～")
else:
    print("您输入的数值不在可计算范围内")


