import numpy as np
import matplotlib.pyplot as plt


x = np.array([3,0,2])
y = np.array([1,5,7])

# plt.plot(x, y)
# plt.plot(x, y , linestyle = 'dotted')
plt.plot(x, y , linestyle = 'dashed' ,marker  = 'o' , ms = 12 , mec = "r", mfc = "r") 
plt.show()

'''
Line Color
You can use the keyword argument color or the shorter c to set the color of the line:
'''

# plt.plot(x, y , color = 'g' ,marker  = 'o' , ms = 12 , mec = "r", mfc = "r") 
# plt.show()


'''
Line Width
You can use the keyword argument linewidth or the shorter 
lw to change the width of the line.

The value is a floating number, in points:
'''

# plt.plot(x, y ,linewidth = '8',marker  = 'o' , ms = 12 , mec = "r", mfc = "r") 
# plt.show()


# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt .plot(x1,y1 , color = 'r', marker = 's', ms = 8 , mec = 'g' , mfc = 'g')
# plt .plot(x2,y2 ,color = 'b', marker = 'o', ms = 8 , mec = 'k' , mfc = 'k')
# plt.show()




