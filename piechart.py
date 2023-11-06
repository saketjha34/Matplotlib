import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math


'''
Air is made up of 78.09% nitrogen, 20.95% oxygen, 
0.93% argon, 0.04% carbon dioxide, 
and other gases in meagre amounts
'''


'''
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White
'''

y = np.array([78.09 , 20.95, 0.93, 0.03])
x_labels = np.array(["Nitrogen" , "Oxygen","Argon","Carbon Dioxide"])

explode = np.array([0,0.1,0.1,0.3])

colors = np.array(["r" , "g","b","c"])

# plt.pie(y, labels = x_labels)

# plt.pie(y, labels = x_labels  , startangle = 90)

# plt.pie(y, labels = x_labels  , explode = explode)

plt.pie(y, labels = x_labels  , explode = explode , colors = colors)

plt.legend(title = "Air Constituent")
plt.show()








