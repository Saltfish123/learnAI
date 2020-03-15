# -*- coding: utf-8 -*-
import numpy as np

# 获取矩阵中每一列的最大索引值位置
data = np.sin( np.arange( 20 ).reshape( 5,4 ))
print( data )
index = data.argmax( axis = 0)
print( index )
# 根据获取最大索引值位置获取矩阵每一列的最大值
data_column_max = data[range( data.shape[1] ),index]
print( data_column_max  )
# 获取矩阵中每一行最大索引值的位置
index = data.argmax( axis = 1 )
# 获取矩阵中每一行最大索引值的位置获取每一行最大值
print([ range(data.shape[0]),index ])
data_row_max = data[range( data.shape[0]),index ]
print( data_row_max )

'''
02 对矩阵进行扩展操作
'''
a = np.arange(0,40,10)
print( a )
b = np.tile( a,[3,3])
print( b )

'''
03 数组的排序操作
'''
a = np.array([
    [1,7,3],
    [4,9,6],
    [7,8,9]
])
print( a )
# 对矩阵每一列中所有元素进行从大到小排序
b = np.sort( a,axis = 0 )
print( b )
# 获取矩阵排列数序从小到大的的索引值
a = np.array([1,4,3,2])
print( a )
j = np.argsort( a )
print( j )
# 通过索引值得出矩阵的排序结果
print( a[j] )
