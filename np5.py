# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

a = np.array([0, 30, 90])
b = np.sin(a * np.pi / 180) #sin(弧度） 角度 * π /180 = 弧度
print(b)

c = np.degrees(np.pi / 2) #弧度转角度
print(c)  