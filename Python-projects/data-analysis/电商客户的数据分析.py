import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#解决中文乱码
plt.rcParams['font.family']=['Microsoft Yahei','SimHei','sans-serif']
data = {
    'name': ['张三', '李四', '王五', '李四', '王五', '王五', '赵六'],
    'chinese': [18, 53, 67, 63, 39, 70, 94],
    'math': [82, 63, 41, 59, 46, 39, 58],
    'english': [68, 52, 90, 86, 60, 98, 64],
    'week': ['一', '一', '一', '二', '二', '三', '一']
}
df=pd.DataFrame(data)
print(df.info())
print(df.describe())
print(df.head())
df2=df.loc[0:4,'chinese':'english']
df3=df2.copy()
df4=df3.copy()
df4["score_qcut"]=pd.qcut(df.chinese,3,labels=["低分","中分","高分"])
print(df4['score_qcut'])
print(df4.score_qcut.value_counts().plot.pie(
    autopct='%1.f%%'
))