MATPLOTLIB
----------
-->This is a library in python for data visualization, allowing users to create a variety of plots...

Basic Structure of Matplotlib
-----------------------------
-->Figure
-->Axes
-->Axis
-->Grid
-->Title
-->Legend

-->Figure
---------

BAR GRAPH
---------

import matplotlib.pyplot as plt
Sales = ['A', 'B', 'C']
Values = [25, 30, 45]
plt.bar(Sales,Values,color = 'pink', edgecolor = 'black')
plt.xlabel('Car models')
plt.ylabel('Values')
plt.title('BWM Sales')
plt.show()

LINE PLOT
---------

import matplotlib.pyplot as plt
Sales = ['A', 'B', 'C']
Values = [25, 30, 45]
plt.plot(Sales,Values,color = 'blue')
plt.xlabel('Car models')
plt.ylabel('Values')
plt.title('BWM Sales')
plt.show()

import matplotlib.pyplot as plt
overs = [1,2,3,4,5]
score = [4,9,17,20,8]
plt.plot(overs, score, color = 'pink')
plt.title('Score Card')
plt.xlabel('Overs')
plt.ylabel('Score')
plt.show()

PIE CHART
---------
import matplotlib.pyplot as plt
subjects = ['Python', 'Java', 'DA']
students = [35,7,25]
plt.pie(students,labels = subjects, autopct = '%1.1f%%')
plt.legend(subjects)
plt.title('Students in Courses')
plt.show()

SCATTER->Dots
-------

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [10,15,18,20,15,11]
plt.scatter(x,y)
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()



HISTOGRAM
---------

import matplotlib.pyplot as plt
y = [10,15,18,20,15,11]
plt.hist(y, color = "lightblue", edgecolor = "black")
plt.title('Histogram Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()



import matplotlib.pyplot as plt
Sales = ['A', 'B', 'C']
Values = [25, 30, 45]
plt.plot(Sales,Values,color = 'blue', linestyle = '-.', marker = "o", markerfacecolor = "lightblue")
plt.xlabel('Car models')
plt.ylabel('Values')
plt.title('BWM Sales')
plt.show()
















































