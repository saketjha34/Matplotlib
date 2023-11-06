import numpy as np
import matplotlib.pyplot as plt
import math

# <-----------ploting xi + yj vector field--------->

# x = np.linspace(-10,10,11)
# y = np.linspace(-10,10,11)
# (x,y) = np.meshgrid(x,y)
# u = x
# v = y
# plt.quiver(x,y,u,v)
# plt.show()

# <-----------ploting sin(x)i + cos(y)j vector field--------->

# x = np.linspace(-10,10,11)
# y = np.linspace(-10,10,11)
# (x,y) = np.meshgrid(x,y)
# u = np.sin(x)
# v = np.cos(y)
# plt.quiver(x,y,u,v)
# plt.show()


# <-----------ploting sin(x)i + e^(x^2)j vector field--------->

# x = np.linspace(-10,10,11)
# y = np.linspace(-10,10,11)
# (x,y) = np.meshgrid(x,y)
# u = np.sin(x)
# v = (-np.e)** (x**2)
# plt.quiver(x,y,u,v)
# plt.show()

# <-----------ploting -sin(y)i + cos(x)j vector field--------->

x = np.linspace(-10,10,11)
y = np.linspace(-10,10,11)
(x,y) = np.meshgrid(x,y)
u = -np.sin(y)
v = np.cos(x)
plt.quiver(x,y,u,v)
plt.show()

