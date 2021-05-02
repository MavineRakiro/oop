import numpy as np
import matplotlib.pyplot as plt
import math 

x = np.arange(-7, 7, 0.001)

def normal_distribution(x, mean, std):
    outer = 1 / std * np.sqrt(2 * math.pi)
    inner = np.exp(-0.5 * (x-mean / std)**2)
    return outer * inner 

y = normal_distribution(x, 0, 1)

dists= [
    {'mean':0, 'std':1, "color":"r", "style":"--"},
    {'mean':2, 'std':1, "color":"m", "style":"-."}
]

plt.figure(figsize=(6.5,4.5))
for dist in dists:
    y = normal_distribution(x, dist["mean"], dist["std"])
    plt.plot(x, y, 
    label=f"mean: {dist['mean']} std {dist['std']}",
    color=dist["color"], 
    linestyle=dist["style"])
    plt.xlim([-7, 7])
    plt.ylim
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("$\\frac{1}{\sigma\sqrt{2\pi}}$", rotation=-45)
    plt.title("Normal distribution")
plt.legend()
plt.show()




