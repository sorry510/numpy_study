# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

# 数据类型
# dt = np.dtype([('test1', 'i1'), ('test2', 'f4')])
# a = np.array([[1,2,3,4,5],
# 			  [6,7,8,9,10]], dtype = dt)
# print(a['test1'])

# 转换数组
# a = np.array([[1,2,3],
# 			  [4,5,6]])
# a.shape = (3, 2)
# print(a)


# a = np.array([[1,2,3],[3,4,5]], dtype = 'f4')
# print(a.ndim) #维度
# print(a.itemsize)


a = np.empty([3, 2], dtype = np.int8)
print(a)
# a = np.zeros([3, 2], dtype = float)
# print(a)


# a = np.zeros([3, 2], dtype = [('x', 'i1'), ('y', 'i1'), ('z', 'f2')])
# print(a)
# print(a['x'])


# a = np.ones([2, 3])


# a = np.arange(5, dtype = float)
# print(a)


# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a[:, 1:2]) #数组维数不变，取每一行的第二列
# print(a[..., 1]) #第二列
# print(a[1, ...]) #第二行


# x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
# y = x[[0,1,2],  [0,1,0]]  
# print(y)
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
# rows = np.array([[0,0],[3,3]])
# cols = np.array([[0,2],[0,2]]) 
# y = x[rows,cols]
# # y = x[[[0,0],[3,3]], [[0,2],[0,2]]]  
# print(y)


# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print(x[x > 5])


# a = np.array([1., 2+6j, 5, 3.5+5j])  
# print(a[np.iscomplex(a)])  


# a = np.arange(0,60,5) 
# a = a.reshape(3,4) #转换为3行4列
# b = a.T #转置矩阵  
# print('原始数组是：')  
# print(a)  
# print('修改后的数组是：')  
# for x in np.nditer(a):  
#     print(x)