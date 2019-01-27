# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

arr = np.array([1,2,3,4])

#arr.mean() #平均数
std = np.std(arr) #标准差std = sqrt(mean((x - x.mean())**2))
var = np.var(arr) #方差（标准差的平方	）