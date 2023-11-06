import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':25}


x = np.array([2,3,5,9,0])
y = np.array([1,8,1,4,1])

# plt.plot(x,y)
# plt.title("X-Y Axis Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.show()

plt.plot(x,y)
plt.title("X-Y Axis Plot")  
plt.xlabel("X-Axis" , fontdict = font1)
plt.ylabel("Y-Axis" , fontdict = font2)
plt.show()


