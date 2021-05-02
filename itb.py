a = 5
b = 3.24
c = [1, 2, 3]
d = {"CBD": 100, "Rongai": 20 }
e = (1, 2, 3)
f = set(c)
f = {1, 2, 3}

"""
name = input("Enter name:")
print(name)
print(type(name))
number = int(input("Enter number: "))
number = float(input("Enter number: "))
a = 3.14159
print("The number is", a)
print("The number is {} and {:.3f}".format(a, a))
print("The number is %f and %.2f" %(a, a))
print(f"The number is {a} and {a:.2f}")

a = [1, 2, 3]
for m in a:
    print(m)

for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 1, -2):
    print(i)

a = [1, 2, 3, 4, 5]

new_a = []
for i in a:
    new_a.append(i ** 2)
print(new_a)

sq_a = [i**2 for i in a]
print(new_a == sq_a)

print(a)
print(a[0])
print(a[:4])
print(a[-2])
print(a[-1:1:-1])
print(a[::-
stomach = 0
spoon = 15
hungry = True
a = True
b = False
print(type(a))
print(not a)
print(a and b)
print(a or b)

a = 1
if a > 10:
    print("A > 10")
else:
    print("A is not > than 10")

age = 37
if age < 12:
    print("Child")
elif age < 20:
    print("Teenage")
elif age < 35:
    print("Youth")
elif age < 50:
    print("Middle-aged")
elif age < 100:
    print("Retired")
else:
    print("Are you a vampire?")

age = 13
if age < 18:
    print("Under 18")
    if age <= 12:
        print("Child")
    else:
        print("Teenager")
else:
    print("Over 18")

# ==, <, >, <=, >=, !=

stomach = 0
spoonful = 15
hungry = True

while hungry:
    stomach = stomach + spoonful # stomach += spoonful
    if stomach >= 100:
        hungry = False # hungry = not hungry
    print(f"You are now {stomach}% full")

for i in range(11):
    if i == 5:
        break
    print(i)

for i in range(11):
    if i == 5:
        continue
    print(i)


stomach = 0
spoon = 20

while True:
    stomach += spoon
    print(f"{stomach} % full")
    if stomach >= 100:
        break
    # print("{} % full".format(stomach))

students = {
    "One": 90,
    "Two": 88,
    "Three": 92
}
print(students)
print(type(students))
print(students["One"])
print(students.get("Three"))

students["One"] = 47
for i, j in students.items():
    print(i, j)

foods = ["veg", "meat", "rice"]
for food in foods:
    print(food)
    print(food.capitalize())
    print(food.lower())

for index, food in enumerate(foods):
    print(index, food)
"""

foods = ['veg', 'rice', 'beef']
shopping = ['books', 'electronics', 'bike']
# len(foods)

for i, j in zip(foods, shopping):
    print(i, j)