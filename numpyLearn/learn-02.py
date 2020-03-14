# -*- coding: utf-8 -*-
import numpy as np

'''
01 矩阵元素的判断与比较
'''
# 判断矩阵中是否存在某一定义的值
vector = np.array([5,10,15,20])
print( vector == 10 )
matrix = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print( matrix == 25 )

'''
02 矩阵判断后返回结果的索引应用
'''
# 获取矩阵中的索引位置
second_column_25 = ( matrix[:,1]==25)
print( second_column_25 )
# 获取元素值等于25的行元素
print( matrix[second_column_25,:])
# 获取元素值等于25的列元素
print( matrix[:,second_column_25])

'''
03 矩阵中的与或关系判断
'''
vector = np.array([5,10,15,20])
equal_to_ten_and_five = ( vector == 5 ) & ( vector == 15)
print( equal_to_ten_and_five )
equal_to_ten_or_five = ( vector == 5 ) | ( vector == 15 )
print( equal_to_ten_or_five )
# 利用返回True结果的索引对矩阵重新复制
vector[equal_to_ten_or_five] = 50
print( vector )
matrix = np.array([
    [5,10,15,20],
    [25,30,35,40],
    [45,50,55,60],
])
second_column_25 = matrix[:,0] == 25
print( second_column_25 )
matrix[second_column_25,3] = 10
print( matrix )
'''
04 矩阵的类型转换
'''
vector = np.array(["5","10","15","20"])
print( vector.dtype )
# 字符串转换float类型
vector = vector.astype( float )
print( vector )
print( vector.dtype )
'''
05 矩阵中的最大值和最小值
'''
vector = np.array([5,10,15,20])
print( vector.max( ))
print( vector.min( ))
matrix = np.array([
    [5,10,15,20],
    [25,30,35,40],
    [45,50,55,60]
])
#指定矩阵某一列获取最大值
print(matrix[:,0].max())
#指定矩阵某一行获取最大值
print(matrix[2:3,:].max())
'''
06  数组的求和操作
'''
# 指定矩阵列进行求和
print( matrix.sum( axis = 0 ))
# 指定矩阵行进行求和
print( matrix.sum( axis= 1 ))

