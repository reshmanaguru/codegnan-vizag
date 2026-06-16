DATA ANALYSIS
-------------
-->This is process of inspecting,cleaning,transfroming and modeling data to discover useful insights...

1.DESCRIPTIVE ANALYSIS
----------------------
-->Summarizing Data

2.DIAGNOSTIC ANALYSIS
---------------------
-->Understanding Causes

3.PREDICTIVE ANALYSIS
---------------------
-->Forecasting future outcomes

4.PRESCRIPTIVE ANALYSIS
-----------------------
-->Suggesting actions based on data

WHY DA
-------
-->To improve decision making
-->Detects trends & patterns

NUMPY(Numerical python)
-----------------------
--> Tghis python library for numerical computing. it provides support for multi-dimensional arrays, and linear algebra operations, making it essentials for data analysis...

Using numpy in DA
-----------------
-->Improved performance
-->Simplifies complex operations
-->Easy data manipulation...

import numpy as np
arr_1=np.array([1,2,3,4])
print(arr_1)

import numpy as np
arr_1=np.array([[4,5,6,7],[1,2,3,4],[5,6,7,9]])
print(arr_1)

import numpy as np
arr_1=np.array([[1,2,3],[4,5,6]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshape(3,2)
print(reshaped)

import numpy as np
arr_1 = np.array([10,20,30,40,50])
print(arr_1[4])
print(arr_1 + 5)

import numpy as np
arr_1 = np.array([[1,2],[3,4]])
arr_2 = np.array([[5,6],[7,8]])
print(np.dot(arr_1, arr_2))

import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)

copy_dee = arr_1.copy
arr_1[1] = 300
print(copy_dee)
print(arr_1)


PANDAS
------
-->Tha pandas is a powerful data manipulation and analysis library..
-->Where it provides data structure like series and dataframe for efficient data handling...

METHOD SERIES
-------------
mean()
sum()
max()
min()
apply()
map()


import pandas as pd
any = pd.Series([2999,15999,52999,4999,1999],index = ['Earbuds', 'Smartphone', 'Lap', 'Watch', 'Footware'])
print(any)

Dataframe
---------
import pandas as pd
data = {'Product':['Earbuds','Smartphone','Lap','Watch','Footware'],
        'Brand':['Noise','oneplus','Hp','Bolt','Nike'],
        'Price':[1599,15999,53999,1999,3999],
        'Stock':[50,15,25,40,70]}
dip = pd.DataFrame(data)
print(dip)








































