#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 我们在写Python的相信大家会遇到过同样的错误，执行时报错"AttributeError: 'module' object has no attribute 'urlopen'"
# 分析导致报错的原因，系统存在过期库，
# pip list  #列出所有安装的库
# pip list --outdated #列出所有过期的库
# 提供自动更新程序如下：
'''
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
'''
a = 2
b = 3
c = a**b
print "6 - c 的值为：", c