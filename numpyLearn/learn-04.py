# -*- coding: utf-8 -*-
import numpy as np
'''
01 矩阵的特殊形式数学运算
'''
A = np.arange(3)
print( A )
# 矩阵开平方运算
print( np.sqrt( A ))

'''
03 向下取整函数( floor )
'''
a = np.floor( 10 * np.random.random(( 3,4 )))
print( a )
# 查看矩阵类型
print( a.shape )
# 查看矩阵维度
print( a.ndim )
# 矩阵转换成一维向量
print( a.ravel() )
# 矩阵进行维度转换
a.shape = (2,6)
print( a )
# 矩阵的置换操作
print( a.T )

'''
04 矩阵的拼接操作
'''
a = np.floor( 10 * np.random.random(( 3,4 )) )
print( a )
b = np.floor( 10 * np.random.random(( 3,4 )))
print( b )
# 矩阵进行按行拼接
print( np.hstack( (a,b) ))
# 矩阵进行按列拼接
print( np.vstack(( a,b )))
a = np.floor( 10*np.random.random( (3,4) ))

'''
05 矩阵的切分操作
'''
a = np.floor( 10 * np.random.random(( 2,12 )))
print( a )
# 对矩阵按行进行分割
print( np.hsplit( a,3 ))
# 对矩阵指定位置进行分割
print(np.hsplit( a,( 3, 4 ) ) )
# 对矩阵进行按列分割
b = np.floor( 10 * np.random.random( ( 12, 2 )))
print( b )
print( np.vsplit( b,(5,6) ))

'''
06 矩阵的复制操作
'''
a = np.arange( 12 )
b = a
print( b )
# 对b矩阵进行维度转换 a矩阵维度也会发生相应的变化
b.shape = ( 3,4 )
print( a )

'''
07 矩阵的浅复制操作
'''
c = a.view()
print( c )
# 对c矩阵的维度转换 a矩阵的维度也不会改变
c.shape = ( 2,6 )
print( c )
print( a )
# 对c矩阵的某一元素进行改变 a矩阵中的元素会发生变化
c[1,1] = 3333
print( c )
print( a )

'''
08 矩阵深复制操作
'''
d = a.copy()
# 对d矩阵进行维度转换 a矩阵的维度不会发生改变
d.shape = (6,2 )
# 对d矩阵的某一元素进行改变 a矩阵元素不会发生变化
d[1,1] = 555
print( d )
print( a )




