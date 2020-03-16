# -*- coding: utf-8 -*-
import pandas as pd

'''
01 pandas 文件的基本操作
'''
#读取csv文件操作
food_info = pd.read_csv("food_info.csv")
# 获取前三行数
print( food_info.head( 3 ))
# 查看数据类型
print( type( food_info ))
# 查看数据结构
print( food_info.dtypes )
# 查看尾部数据
print( food_info.tail( 4 ))
# 显示所有列名
columns_names = food_info.columns
print( columns_names )
# 查看维度信息
print( food_info.shape )