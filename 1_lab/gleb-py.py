# i
print("=== Типи даних ===")
text_var = "Hello World"
num_int = 42
num_float = 3.14
my_list = ["Python", 2025, 9.81, text_var]
my_dict = {"lang": "Python", "year": 2025, text_var: num_int}
my_tuple = ("tuple", text_var)
my_set = {"set_item", text_var + str(num_int)}

print(text_var, type(text_var))
print(num_int, type(num_int))
print(num_float, type(num_float))
print(my_list, type(my_list))
print(my_dict, type(my_dict))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))

# ii
print("\n=== Вбудовані константи ===")
print("Константа 1:", True)
print("Константа 2:", False)
print("Константа 3:", None)



# iii
print("=== Вбудовані функції ===")
print(abs(2345.7), f"це рівним {abs(2345.7)}")
print(round(3.14159, 2))
print(len("Python"))

# iv
print("\n=== Цикли ===")
letters = ["d", "g", "y"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

for num in range(1, 4):
    print(f"Це число {num}")

# v
print("\n=== Розгалуження ===")
A = True
if A:
    print("Значить B=True")
else:
    print("Значить B=False")

x = 10000
if x > 0:
    print("x додатній")
elif x < 0:
    print("x від’ємний")
else:
    print("x дорівнює нулю")

# vi. try -> except -> finally
print("\n=== try-except-finally ===")
A = 97
try:
    print("Що буде якщо:", 10 / A, "???")
except Exception as e:
    print("Помилка:", e)
finally:
    print("А вот воно що!")

# vii
print("\n=== Контекст-менеджер with ===")

with open("test.txt", "w") as f:
    f.write("Привіт з Python!\nЦе приклад контекст-менеджера.")

with open("test.txt", "r") as f:
    for line in f:
        print("З файлу:", line.strip())

# viii
print("\n=== Lambda ===")
this_is_lambda = lambda first, last: f"Цей код написав: {first} {last}"
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda("Гліб", "Марходей"))
