import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = 2 * np.random.rand(100, 1)

y = 4 + 3 * x + np.random.randn(100, 1)

#plt.scatter(x, y, s = 5.0)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()

# if the data had no noise

#y = 4 + 3 * x

#plt.plot(x, 4 + 3 * x)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()


#Normal Equation.

x_b = np.c_[np.ones((100, 1)), x]
cost_function = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)

print(cost_function)

x_new = np.array([[0], [2]])

x_new_b = np.c_[np.ones((2, 1)), x_new]
# what is np.c_[.... and why the two brackets for 2, 1

y_predict = x_new_b.dot(cost_function)

print(y_predict)

#plt.scatter(x, y, s = 5.0)

#plt.plot(x_new, y_predict, 'r--')
#plt.axis([0, 2, 0, 15])
#plt.show()


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def derivative(f, z, eps = 0.000001):
    return(f(z +eps) - f(z)) / eps

x = np.linspace(-8, 8, 1000)
y = sigmoid(x)
y_der  = derivative(sigmoid, x)

plt.plot(x, y, 'b-', label = "Sigmoid : $\phi(z)$")
plt.plot(x, y_der, 'r-.', label = "Sigmoid derivative : $\phi'(z)$")
plt.axis([-8, 8, 0, 1.0])
plt.xlabel('z')
plt.legend()
plt.ylabel(f'$\phi(z)$')
plt.grid(True)
plt.title('Sigmoid funtion $\phi(z)$')
plt.show()