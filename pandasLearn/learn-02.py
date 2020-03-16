# -*- coding: utf-8 -*-
import pandas as pd

'''
01 pandas 数据的数学运算
'''

food_info = pd.read_csv("food_info.csv")
print( food_info )
# 将mg --> g
div_1000 = food_info["Iron_(mg)"]/1000
print( div_1000 )

'''
02 pandas 数据整合操作
'''
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print( water_energy )

# 将mg指标转换成g并进行数据添加
iron_grams = food_info["Iron_(mg)"] / 1000
print( food_info.shape )
# 添加一行数据
food_info["Iron_(g)"] = iron_grams
print( food_info.shape )

'''
03 pandas 最值操作
'''
max_calories = food_info["Energ_Kcal"].max()
print( max_calories )
# 求出每一列数据的最大值占比
normalized_calories = food_info["Energ_Kcal"] / max_calories
print( normalized_calories )
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
print( normalized_protein )

'''
04 pandas 数据的升降序操作
'''
# 升序
food_info.sort_values("Sodium_(mg)",inplace=True )
print( food_info["Sodium_(mg)"])
# 降序
food_info.sort_values("Sodium_(mg)",inplace=True,ascending=False)
print( food_info["Sodium_(mg)"])