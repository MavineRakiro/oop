import matplotlib.pyplot as plt
import numpy as np
import math
#import random

"""
#from scipy import sparse

a = np.array([12])
b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
c = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])
d = np.ones((4, 4))
e = np.identity(4)

print(c)
print(c[1])
print(c[1, 3])
print(c[0, 1:3])

sub_matrix = print(c[ : ,1: 5: 2])

#matrix_sparse = sparse.csr_matrix(e)
#print(matrix_sparse)

print(c.shape)
print(c.size)
print(c.ndim)

# How is lambda used?
#add = lambda c : c + 100
#print(add)

# Mean, Variance, Standard Deviation

print(np.mean(c))
print( np.mean(c) == np.sum(c.flatten()) / c.size)

print(np.var(c))
print(np.std(c))

print(c.reshape(5, 3))
print(c.reshape(15, 1))
print(c.reshape(1, 15).ndim)
print(c.flatten().ndim)

print(c.reshape(c.size))

print(c.transpose())
print(np.linalg.det(d))
print(c.diagonal())
c.diagonal(offset = -1)
c.diagonal(offset = 1)
print( c.trace() == sum(c.diagonal()))

# eigenvalues, eigenvectors = np.linalg.eig(matrix)


s = np.array([1 ,2 , 3, 4])
h = np.array([5, 6, 7, 8])

np.dot(s, h)
print(np.dot(s, h) == s@h)
s*h
np.add(s, h)
np.subtract(s, h)

s + h
s - h

z = np.array([
    [4.3, 5],
    [9, 8.2]
])
y = np.linalg.inv(z)
print(z *y)

print(np.random.random(4))

np.random.randint(0,11, 5)
np.random.normal(0.0, 10.0, 12)


#Graphical distribution.

x = np.arange(-7, 7, 0.01)

def normal(x, mean, std):
    p = 1 / std * np.sqrt(2 * math.pi)
    q = np.exp(-.5 / std**2 * (x - mean) ** 2)
    return p*q

parameters = [
    {'mean': 0,
    'std': 1},
    {'mean': 3,
    'std': 2},
    {'mean': 5,
    'std': 1}
]
normal_dist = []
for i in parameters:
    output_values = normal(x, i['mean'], i['std'])
    normal_dist.append(output_values)

normal_dist = np.array(normal_dist)

plt.figure(figsize = (6.5, 4.5))

for i in range(3):
    plt.plot(x, normal_dist[i])
    #label = f"mean : {dict['mean']} std: {dict['std']}")
    plt.legend()
    plt.grid(True)  

plt.show()

num = str(42)
num1 = []
num1 = num1.append(i for i in num)
print(num1)

#def expanded_form(num):
    #num1 = num % 10
    #num2 = num.split(i for i in range(num))
    #print(num2)

#for i in range(num):
 #   num3 = i
  #  if num3 % 10 == 0:
   #     num4 = print(num3)


np.random.seed(42)

x = 2 * np.random.rand(100, 1)

y = 4 + 3 * x + np.random.randn(100, 1)

plt.scatter(x, y, s = 5.0)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(x, 4 + 3 * x)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""



         