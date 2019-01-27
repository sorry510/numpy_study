# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

# a = np.arange(9).reshape(3, 3)
# print(a)
# print(a.flat[5])
# print(a.flatten())


# a = np.arange(8).reshape(2,2,2)
# print(a)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
ab = np.concatenate((a, b)) #沿轴 0 连接两个数组
ab1 = np.concatenate((a, b), axis = 1) #沿轴 1 连接两个数组
print(ab)