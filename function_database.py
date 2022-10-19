#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:27:32 2022

@author: muzian
"""
import sys

def mod_choose(mode):
    if mode == 1:
        print("请稍等")
    elif mode == 2:
        print("该模式正在开发中，暂时无法响应")
        sys.exit()
    else:
        print("您输入的内容超出运行范围")
        sys.exit()
    return

def year_0_5():
    score_0_5 = float(input("请输入您当前的总GPA"))
    
    return
    
