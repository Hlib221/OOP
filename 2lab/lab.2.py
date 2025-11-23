#1
text1 = "Hello World"
number1 = 42
float1 = 99.99
list1 = [10, 20, 30, "Python", 3.14]
dict1 = {"name": "John", "age": 25, "city": "Lviv"}
tuple1 = (100, 200, "data")
set1 = {1, 2, 3, 4, 5}

print(f"text1 = {text1}, type: {type(text1)}")
print(f"number1 = {number1}, type: {type(number1)}")
print(f"float1 = {float1}, type: {type(float1)}")
print(f"list1 = {list1}, type: {type(list1)}")
print(f"dict1 = {dict1}, type: {type(dict1)}")
print(f"tuple1 = {tuple1}, type: {type(tuple1)}")
print(f"set1 = {set1}, type: {type(set1)}")

#2
divisor = 0
try:
    result = 10 / divisor
    print(result)
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Виконання завершено")

#3
file_name = "readme.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")
    f.write("Fourth line\n")
    f.write("Fifth line\n")

with open(file_name, "r", encoding="utf-8") as f:
    for index, content in enumerate(f):
        print(f"{index}: {content.strip()}")


#4
def func1(x, y):
    return x, y

lambda1 = lambda name, age: f'{name}, вік: {age}'
print(lambda1("Іван", 25))
print(lambda1(*func1("Петро", 30)))

add = lambda x, y: x + y
square = lambda x: x ** 2
print(f"5 + 3 = {add(5, 3)}")
print(f"7^2 = {square(7)}")

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(f"Квадрати: {squared}")


#5
print(f"True: {True}")
print(f"False: {False}")
print(f"None: {None}")

import sys
help("keywords")


#6
print(abs(-15), abs(15), abs(-15) == abs(15))

list2 = [10, 20, 30, 40, 50]
print(f"len: {len(list2)}")
print(f"max: {max(list2)}")
print(f"min: {min(list2)}")
print(f"sum: {sum(list2)}")

num3 = 3.7856
print(f"round: {round(num3, 2)}")


#7
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"{i}: {letters[i]}")

count = 1
while count <= 5:
    print(count)
    count += 1

for i in range(1, 6):
    if i == 3:
        break
    print(i)


#8
from random import randint

x = randint(0, 10)
if x < 5:
    print(f"{x} < 5")
elif x < 8:
    print(f"5 <= {x} < 8")
else:
    print(f"{x} >= 8")

age = 22
if age < 18:
    print("Неповнолітній")
elif age < 65:
    print("Дорослий")
else:
    print("Пенсіонер")
