from __future__ import print_function
import pandas as pd

data=pd.read_excel('D:/各类数据/因子分析数据.xlsx',index_col=u'地区',sheetname="Sheet2")

a=data.corr() #相关系数矩阵，即给出了任意两个指标之间的相关系数
b=data.corr()[u'A'] #只显示“A”指标与其他指标的相关系数
c=data[u'A'].corr(data[u'B']) #计算“A”指标与“B”指标的相关系数

print(a)
print(b)


#计算两个列向量的相关系数，采用Spearman方法
D=pd.DataFrame([range(1,8),range(2,9)]) #生成样本D，一行为1~7，一行为2~8
D.corr(method='spearman') #计算相关系数矩阵
S1=D.loc[0] #提取第一行
S2=D.loc[1] #提取第二行
c=S1.corr(S2,method='spearman') #计算S1、S2的相关系数
print(c)

#计算6x5随机矩阵的协方差矩阵

import numpy as np
D=pd.DataFrame(np.random.randn(6,5)) #产生6x5随机矩阵
d=D.cov() #计算协方差矩阵
print(d)
e=D[0].cov(D[1]) #计算第一列和第二列的协方差
print(e)

#计算6x5随机矩阵的偏度/峰度
D=pd.DataFrame(np.random.randn(5,4))
m=D.skew()
n=D.kurt()
print(m)
print(n)




