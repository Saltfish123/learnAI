# -*- coding: utf-8 -*-
import  numpy as np
'''
01 矩阵的转换操作
'''
# 根据范围创建矩阵进行结构限制
a = np.arange( 15 ).reshape(3,5)
print( a )
# 查看矩阵的行和列( shape )
print( a.shape )
# 查看矩阵维度( ndim )
print( a.ndim )
# 查看矩阵类型 ( dtype )
print( a.dtype )
# 查看矩阵元素个数( size )
print( a.size )

'''
02 矩阵的初始化操作
'''

# 定义 所有元素等于0的3x4矩阵
zeros = np.zeros(( 3,4 ))
print( zeros )
# 定义所有元素等于0的3x4矩阵 并限制矩阵类型
zeros = np.zeros(( 3,4 ),dtype = np.int32 )
print( zeros )
print( zeros.dtype )
# 定义所有元素等于1的5x2矩阵 并限制矩阵类型
ones = np.ones(( 5,2 ),dtype = np.str )
print( ones )

'''
03 矩阵中步长操作
'''
a = np.arange( 10, 30, 5 )
print( a )
b = np.arange( 0, 2, 0.3 )
print( b )

'''
04 矩阵中随机数列操作
'''
# 随机获取 0-1范围内 10个随机数
a = np.random.random(  ( 1, 10 ) )
print( a )

'''
05 矩阵中的π和linspace函数应用
'''
# 创建 带有0.2*π 的100个平均分布的元素矩阵
a = np.linspace( 0.2 * np.pi, 100)
print( a )

'''
06 sin函数的使用
'''
a = np.sin( np.linspace( 0.2 * np.pi , 100 ))
print( a )

'''
07 矩阵中的数学运算
'''
a = np.array([ 5,10,15,20 ])
b = np.arange( 4 )
print( a )
print( b )
# 行相减
c = a - b
print( c )
# 计算矩阵的开方
print( b ** 2 )
# 矩阵判断操作
print( a < 15 )
# 矩阵中的乘法运算
A = np.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
])
B = np.arange(9).reshape(3,3)
print( B )
# 对应位置进行相乘
print( A*B )
# 矩阵中dot乘法( 行 * 列 的值相加 )
print( A.dot( B ))




