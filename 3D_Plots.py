import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

ax = plt.axes(projection = "3d")


# <------------------ ploting z = x^2 + y^2 ------------------->

# x = np.linspace(-100,100,3000)
# y = np.linspace(-100,100,3000)
# X , Y = np.meshgrid(x,y)

# Z = X**2 + Y**2

# ax.plot_surface(X,Y,Z , cmap = "plasma")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("x^2 + y^2")
# plt.show()


# <------------------ ploting z = x^2 + y^2 ------------------->

# ax  = plt.axes(projection = "3d")

# x  = np.linspace(-3,3,200)
# y  = np.linspace(-3,3,200)

# X, Y = np.meshgrid(x,y)

# Z = np.sin(X*Y)

# ax.plot_surface(X,Y,Z , cmap = "plasma")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")

# plt.title("sin(xy)")
# plt.show()

# <------------------ ploting z = cot(xy) ------------------->

# ax  = plt.axes(projection = "3d")

# x  = np.linspace(-10,10,200)
# y  = np.linspace(-10,10,200)

# X, Y = np.meshgrid(x,y)

# Z = np.cos(X*Y)/np.sin(X*Y)
# ax.plot_surface(X,Y,Z , cmap = "plasma")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")

# plt.title("cot(xy)")
# plt.show()

