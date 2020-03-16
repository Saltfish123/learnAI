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