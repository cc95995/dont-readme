#绘制直方图

import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
plt.hist(x,10)
plt.show()

#绘制箱型图

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.random.randn(1000)
D=pd.DataFrame([x,x+1]).T#构造两列的DataFrame
D.boxplot()
plt.show()

#绘制x或y轴的对数图形,用plot(logy=True)函数进行

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd

x=pd.Series(np.exp(np.arange(20))) #原始数据
x.plot(label=u'原始数据图',legend=True)
plt.show()
x.plot(logy=True,label=u'对数数据图',legend=True)
plt.show()

#绘制误差条形图

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
import numpy as np
import  pandas as pd

error=np.random.randn(10) #定义误差列
y= pd.Series(np.sin(np.arange(10))) #均值数据列
y.plot(yerr=error) #绘制误差图
plt.show()