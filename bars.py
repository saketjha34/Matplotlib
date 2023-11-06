import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

x = np.array(["Maharashtra" , "Goa" , "Punjab" , "Rajasthan"])
y = np.array([220,115,200,320])

plt.bar(x,y)
# plt.bar(x,y, color = "green")
# plt.bar(x,y, color = "green" , width = 0.2)
# plt.barh(x,y)  # plots bar Horizontaly

plt.xlabel("States")
plt.ylabel("People Per Square KM")
plt.title("Population Density per sq KM")
plt.legend()
plt.show()
