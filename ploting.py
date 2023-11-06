import matplotlib.pyplot as plt
import numpy as np 

'''
 <-----------------Plotting x and y points-------------------->

The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass 
two arrays [1, 8] and [3, 10] to the plot function.
'''

'''
Plotting Without Line
To plot only the markers, 
you can use shortcut string notation parameter 'o', which means 'rings'.
'''

x = np.array([0,10])   
y = np.array([0,20])   

# plt.plot(x,y , 'o')
# plt.show()

'''
Multiple Points
You can plot as many points as
you like, just make sure you have the same number of points in both axis.
'''
x1 = np.array([2,3,5,9,0])
y1 = np.array([1,8,1,4,1])

# plt.plot(x1,y1)
# plt.show()


'''
Default points
If we do not specify the points on the x-axis, they will get the
default values 0, 1, 2, 3 etc., depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, 
the diagram will look like this:
'''

x2 = np.array([2,3,5,9,0])
plt.plot(x2)
plt.show()

