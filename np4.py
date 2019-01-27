# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
a = np.char.center('hello', 20, fillchar = '*')
print(a)
b = np.char.join([':', '-'], ['dmy', 'ymd'])
print(b)