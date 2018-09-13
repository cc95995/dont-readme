#在区间（0<= x <= 2π)绘制一条蓝色的正弦虚线，并在每个坐标点标上五角星。

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure()

import numpy as np
x=np.linspace(0,2*np.pi,50) #x坐标输入
y=np.sin(x) #计算对应x的正弦值
plt.plot(x,y,'bp--') #控制图形格式为蓝色带星虚线，显示正弦曲线
plt.show()

#通过向量[15,30,45,10]画饼图，注上标签，并将第2部分分离出来。

labels='Frogs','Hogs','Dogs','Logs' #定义标签
sizes=[15,30,45,10] #每一块的比例
colors=['pink','gold','black','blue'] #每一块的颜色
explode=(0,0.1,0,0) #突出显示，这里突出显示第二块
plt.pie(sizes,explode=explode,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal') #显示为圆（避免比例压缩为圆）
plt.show()