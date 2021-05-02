"""
import math
import pprint
# print(dir(math))

a = math.log(8 + 1)
b = math.log1p(8)
print(a, b, math.pi)
print(math.inf)
print( a == b)
cos_numbers = []
for i in range(100):
    cos_numbers.append(math.cos(i * 2 * math.pi / 360))
print(cos_numbers)

import mathplt.plot(c
import matplotlib.pyplot as plt
x = [i for i in range(100)]
cos_number = [math.cos(i*2*math.pi/360) for i in range(100)]
# print(cos_numbers == cos_number)
plt.plot(cos_number)
plt.show()
import os
print(os.listdir("../Machine_learning"))

for base_dir, _, j in os.walk("./"):
    print(base_dir)


import helper_file
helper_file.print_hello()

file = open("./venv/pyvenv.cfg")
print(file.read())
file2 = open("sample.txt")
print(file2.read())
import os
# print(os.listdir("./venv/pyvenv.cfg"))

"""

def get_user_input():
    in_ = input("Enter number: ")
    try:
        print(int(in_)/0)
    except ZeroDivisionError:
        print("Number cannot be divisible by zero")
    except ValueError:
        print("Enter valid number")
    # try:
    #     print(in_/0)
    # except:
        # print("Number must be numerical")

get_user_input()

