import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'serif','color':'blue','size':20}
'''
The subplot() Function
The subplot() function takes three arguments that describes 
the layout of the figure.

The layout is organized in rows and columns, 
which are represented by the first and second argument.

The third argument represents the index of the current plot.
plt.subplot(row ,column , index)
'''

# plot 1
x1 = np.array([0,2,3])
y1 = np.array([3,0,2])

plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.title("plot1")

# plot 2 
x2 = np.array([5,7,2])
y2 = np.array([4,9,1])

plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.title('plot2')


plt.suptitle('plots')


plt.show()
