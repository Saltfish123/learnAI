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

'''
07 新索引reset_index 
'''
# 通过年龄建立新的降序排列
new_titanic_survival = titanic_survival.sort_values("Age",ascending=False)
# 创建新的索引
titanic_reindex = new_titanic_survival.reset_index(drop=True)
print( titanic_reindex.head(10) )

'''
08 自定义函数apply应用
'''
# 创建函数返回第100行数据
def hundredth_row( column ):
    hundredth_item = column.loc[99]
    return hundredth_item

hundredth_data = titanic_survival.apply( hundredth_row )
print( hundredth_data )

# 统计所有字段缺失值个数
def field_is_count( column ):

    is_null = pd.isnull( column )

    null = column[ is_null ]

    return len( null )

all_field_count = titanic_survival.apply( field_is_count,axis=0)
print("*-------------------*")
print( all_field_count )
#对各等级船舱进行离散化处理
def which_class( row ):

    pclass = row["Pclass"]

    if pd.isnull( pclass  ):
        return "Unknow"
    if pclass == 1:
        return "First Pclass"
    elif pclass == 2:
        return "Second Pclass"
    else:
        return "Third Pclass"

classes = titanic_survival.apply(which_class,axis=1)
print( classes )
# 计算各等级船舱获救人数的平均值
titanic_survival["classes"] = classes
pclass_surival = titanic_survival.pivot_table( index="classes",values="Survived",aggfunc=np.mean )
print( passenger_survival )

# 对年龄进行离散化处理
def which_age( column ):
    age = column["Age"]
    if pd.isnull( age ):
        return "Unknow"
    elif age < 18:
        return "Minor"
    else:
        return "Adult"
age_labels = titanic_survival.apply( which_age, axis=1)
# 计算各年龄段所在各船舱话费钱的总额
titanic_survival["age_labels"] = age_labels
pay_sum_money = titanic_survival.pivot_table(index="age_labels",values=["Fare"],aggfunc=np.sum )
print( pay_sum_money )


