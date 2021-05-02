"""
def print_hello():
    print("Hello world")

print_hello()

def func():
    hello = "Hello function"
    return hello

# b = func()
# print(b)
# print(hello)

a = [1, 2, 3, 4, 5]

def squares(element):
    return element ** 2

square_a = []
for i in a:
    square_a.append(squares(i))
print(square_a)

a = [1, 2, 3, 4, 5]
def compute(element, value):
    return element ** value

c = []
for i in a:
    c.append(compute(i, 3))
# print(c)

def compute_function(element, value = 3):
    return element ** value

c = [compute_function(i) for i in a]
print(c)

def capital_upper(word):
    return word.capitalize(), word.upper()

name = "StudeNT collEGE"

m, n = capital_upper(name)
print(m, n)

prices = {
    "CBD" : 100,
    "Rongai" : 20,
    "Galleria" : 50,
}
def print_place_prices(in_):
    for key,  value in in_.items():
        print(f"Place : {key} Price : {value}")

print_place_prices(prices)

print("Hello", end=" ")
print("World")
print("Hello\nworld")

def more_args(a, b, *w, **z):
    print(a)
    print(b)
    print(w, w[3])
    print(z, z["k"])

more_args(1, 2, 3, 4, 5, 6, 7, k=4, s=5, v=6)
"""

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func, text):
    a = func(text)
    print(a)

a = "I am a student"
greet(shout, a)
greet(whisper, a)


def create_add(x):
    def add(y):
        return x + y
    return add

add_15 = create_add(15)
b = add_15(17)
print(b)


# print(shout("Hello"))
