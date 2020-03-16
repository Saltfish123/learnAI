# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
'''
01 pandas 数据处理
'''
titanic_survival = pd.read_csv("titanic_train.csv")
print( titanic_survival.head( 3 ))
# 查看年龄数据
age = titanic_survival["Age"]
print( age.loc[3:10] )
# 查看是否存在缺失值
age_is_null = pd.isnull( age )
print( age_is_null )
# 查看缺失值内容
age_null_true = age[ age_is_null ]
print( age_null_true )
# 查看缺失值数量
age_null_count = len( age_null_true )
print( age_null_count )

'''
03 pandas 计算平均数
'''
mean_age = sum( titanic_survival["Age"] ) / len( titanic_survival["Age"])
print( mean_age )
# 取出缺失值
good_age = titanic_survival["Age"][age_is_null==False]
# 计算平均值
correct_mean_age = sum( good_age ) / len( good_age )
print( correct_mean_age )
correct_mean_age = titanic_survival["Age"].mean()
print( correct_mean_age )

'''
04 pandas 求值
'''
# 求各等级船舱人员对应船票的平均价格
passenger_classes = [1,2,3]
fare_by_class = {}
for this_class in passenger_classes:

    pclass_rows = titanic_survival[titanic_survival["Pclass"] == this_class ]

    pclass_fare = pclass_rows["Fare"]
    # 总体求平均数
    fare_by_for = pclass_fare.mean()
    fare_by_class[ this_class ] = fare_by_for
print( fare_by_class )

'''
04 pandas pivot_table 函数应用
'''
# 求各等级船舱平均获救人数
passenger_survival = titanic_survival.pivot_table( index = "Pclass",values="Survived", aggfunc=np.mean )
print( passenger_survival )
# 求等级船舱获取平均年龄
passenger_age = titanic_survival.pivot_table( index="Pclass",values="Age",aggfunc=np.mean )
print( passenger_age )
# 求登船地点总的船票价格和总的获救人数
port_state = titanic_survival.pivot_table( index="Embarked",values=["Age","Survived"],aggfunc=np.sum )
print( port_state )

'''
05 丢掉缺失值操作
'''
drop_na_columns = titanic_survival.dropna(axis = 1)
print( drop_na_columns )
# 丢掉年龄和性别的缺失值
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age","Sex"])
print( new_titanic_survival )

'''
06 pandas 定位操作
'''
# 查看83行的age数据
row_index_83_age = titanic_survival.loc[83,"Age"]
print( row_index_83_age )
# 查看766行的偏差pclass数据
row_index_766_pclass = titanic_survival.loc[766,"Pclass"]
print( row_index_766_pclass )

