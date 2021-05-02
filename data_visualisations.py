import matplotlib.pyplot as plt 
import numpy as np
import math 
"""
x = np.linspace(-10, 10, 1000)
dict = {}
dict["0"] = x ** 2
dict["1"] = x ** 3
dict["2"] = np.log(x)
dict["3"] = np.exp(x)
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.plot(x, dict[str(i)])
plt.ylim([0, 100])
plt.show()

n_rows = 2
n_cols = 2
fig, ax = plt.subplots(n_rows, n_cols)
for i in range(n_rows):
    for j in range(n_cols):
        ax[i, j].plot(x, dict[str(2*i+j)])
        ax[i, j].set_title(f"Figure : {i}")
        ax[i, j].grid(True)
plt.show()

x = np.arange(-10, 10, 0.1)
y = x ** 2
x_min = x[y == np.min(y)][0]
y_min = np.min(y)
print(x_min, y_min)
plt.annotate("Here", xy=(x_min, y_min), xytext=(0,5),arrowprops=dict(arrowstyle="fancy"))
plt.plot(x, y)
plt.show()
"""

x = np.linspace(-8, 8, 10000)
sigmoid = 1 / (1 + np.exp(-x))

tanh = (np.exp(x) - np.exp(-x)) /  (np.exp(x) + np.exp(-x))
tanh_from_sig = 2 * (1 / (1 + np.exp(-2 * x))) - 1

plt.plot(x, sigmoid)
plt.plot(x, tanh)
plt.plot(x, tanh_from_sig)
plt.show()