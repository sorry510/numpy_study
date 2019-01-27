# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

a = np.array([[30,40,0],[0,20,10],[50,0,60]])
zeroIndex = np.nonzero(a)
print(zeroIndex)