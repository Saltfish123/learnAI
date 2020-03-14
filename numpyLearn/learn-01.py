# -*- coding: utf-8 -*-
import numpy as np

'''
01  numpy读取文本操作
'''
world_alcohol = np.genfromtxt("world alcohol.txt",delimiter="	",dtype=str)
# 打印读取结果
print( world_alcohol )
# 打印文本类型
print( type( world_alcohol ) )

'''
02  数组创建
'''
# 创建一维矩阵
vector = np.array([
    5,10,15,20
])
print( vector )
# 创建二维矩阵
matrix = np.array([[0,1,2],[3,4,5],[6,7,8]])
print( matrix )
'''
03 获取矩阵结构( shape )
'''
print( vector.shape )
print( matrix.shape )

'''
04 获取矩阵类型( dtype )
'''
print( vector.dtype )
print( matrix.dtype )
'''
05 改变矩阵元素值的类型 其余元素类型也会发生类型变化
'''
numbers = np.array( [1,2,3,4.0 ] )
print( numbers.dtype )
numbers = np.array( [1,2,3,"4"] )
print( numbers.dtype  )

'''
06 矩阵中元素值得获取
'''
# 获取world_alcohol矩阵中第二行第四列得元素
uruguay_other_1986 = ( world_alcohol[1,3] )
print( uruguay_other_1986 )
# 获取world_alcohol矩阵中第二行第二列得元素
third_country = world_alcohol[2,2]
print( third_country )

'''
07 矩阵得切片方法
'''
matrix = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
])
print( matrix )
# 获取第二列得所有元素
print( matrix[:,1])
# 获取第一列和第二列元素
print( matrix[:,0:2])
# 获取第一列和第三列元素
print( matrix[:,0:2])
# 获取第一行和第三行元素
print( matrix[0::2,:])


