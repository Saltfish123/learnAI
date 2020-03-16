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

'''
02 pandas 切片操作
'''
row_three_to_six = food_info.loc[3:6]
print( row_three_to_six )
# 分别获取每一行对应的数据
row_each_two_to_five_ten = food_info.loc[[2,5,10]]
print( row_each_two_to_five_ten )
# 根据列名获取数据
print(food_info["NDB_No"])
columns_names = "NDB_No"
print( food_info[columns_names])
# 分别获取多行数据
many_names = ["Protein_(g)","Lipid_Tot_(g)"]
print( food_info[ many_names ])

'''
03 pandas 数据的列表转换
'''
col_names = food_info.columns.tolist()
gram_column = []
print( col_names )
# 判断当前行中是否以g为结尾
for c in col_names:
    if c.endswith("(g)"):
        gram_column.append( c )
# 获取以g为结尾的数据
gram_df = food_info[ gram_column ]
print( gram_df.head(3))
