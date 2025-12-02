print("=" * 50)
print("Лабораторна робота 5: ООП")
print("=" * 50)

print("\n--- Завдання 1: Базовий клас Vehicle ---")


class Vehicle:
    """Базовий клас транспортного засобу"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        """Запуск двигуна"""
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} заведено"
        return f"{self.brand} {self.model} вже працює"

    def stop(self):
        """Зупинка двигуна"""
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} зупинено"
        return f"{self.brand} {self.model} вже зупинено"

    def get_info(self):
        """Інформація про транспорт"""
        status = "працює" if self.is_running else "зупинено"
        return f"{self.brand} {self.model} ({self.year}), статус: {status}"


print("\n--- Завдання 2: Наслідування ---")


class Car(Vehicle):
    """Клас легкового автомобіля"""

    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        self.fuel_level = 100

    def drive(self, distance):
        """Їзда на автомобілі"""
        if not self.is_running:
            return "Спочатку заведіть автомобіль!"

        fuel_needed = distance * 0.08
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            return f"Проїхано {distance} км. Залишилось палива: {self.fuel_level:.1f}л"
        return "Недостатньо палива!"

    def refuel(self, amount):
        """Заправка"""
        self.fuel_level = min(100, self.fuel_level + amount)
        return f"Заправлено. Рівень палива: {self.fuel_level:.1f}л"


class Motorcycle(Vehicle):
    """Клас мотоцикла"""

    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def wheelie(self):
        """Трюк на одному колесі"""
        if self.is_running:
            return f"{self.brand} {self.model} робить wheelie! 🏍️"
        return "Заведіть мотоцикл для трюку!"


print("\n--- Завдання 3: Інкапсуляція ---")


class BankAccount:
    """Банківський рахунок з приватними даними"""

    def __init__(self, owner, card_number, balance=0):
        self.owner = owner
        self.__card_number = card_number  # приватне поле
        self.__balance = balance  # приватне поле
        self.__pin = "1234"  # приватний PIN

    def deposit(self, amount):
        """Поповнення рахунку"""
        if amount > 0:
            self.__balance += amount
            return f"✓ Рахунок поповнено на {amount} грн. Баланс: {self.__balance} грн"
        return "✗ Некоректна сума"

    def withdraw(self, amount, pin):
        """Зняття коштів"""
        if pin != self.__pin:
            return "✗ Невірний PIN-код!"

        if amount <= 0:
            return "✗ Некоректна сума"

        if amount > self.__balance:
            return f"✗ Недостатньо коштів. Баланс: {self.__balance} грн"

        self.__balance -= amount
        return f"✓ Знято {amount} грн. Залишок: {self.__balance} грн"

    def get_balance(self, pin):
        """Перевірка балансу"""
        if pin == self.__pin:
            return f"Баланс: {self.__balance} грн"
        return "✗ Невірний PIN-код!"

    def get_masked_card(self):
        """Отримання замаскованого номера картки"""
        return f"**** ** ** {self.__card_number[-4:]}"


print("\n--- Завдання 4: Поліморфізм ---")


class Animal:
    """Базовий клас тварини"""

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Якийсь звук"

    def move(self):
        return f"{self.name} рухається"


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

    def move(self):
        return f"{self.name} біжить на чотирьох лапах"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"
    def move(self):
        return f"{self.name} крадеться на м'яких лапках"


class Bird(Animal):
    def make_sound(self):
        return "Чірік-чірік!"

    def move(self):
        return f"{self.name} летить у небі"


def animal_show(animals):
    """Демонстрація поліморфізму"""
    print("\n Шоу тварин:")
    for animal in animals:
        print(f"  {animal.name}: {animal.make_sound()} - {animal.move()}")


print("\n--- Завдання 5: Система управління ---")

class Student:
    """Клас студента"""

    student_count = 0

    def __init__(self, name, student_id, group):
        self.name = name
        self.student_id = student_id
        self.group = group
        self.grades = []
        Student.student_count += 1

    def add_grade(self, subject, grade):
        """Додати оцінку"""
        if 0 <= grade <= 100:
            self.grades.append({'subject': subject, 'grade': grade})
            return f"✓ Оцінка {grade} з предмету '{subject}' додана"
        return "✗ Оцінка має бути від 0 до 100"

    def get_average(self):
        """Середній бал"""
        if not self.grades:
            return 0
        return sum(g['grade'] for g in self.grades) / len(self.grades)

    def get_info(self):
        """Інформація про студента"""
        avg = self.get_average()
        return f"Студент: {self.name} (ID: {self.student_id}), Група: {self.group}, Середній бал: {avg:.2f}"

    @classmethod
    def get_student_count(cls):
        """Кількість студентів"""
        return f"Всього студентів: {cls.student_count}"


print("\n" + "=" * 50)
print("ТЕСТУВАННЯ ПРОГРАМИ")
print("=" * 50)

print("\n1 Тест Vehicle:")
car1 = Car("Toyota", "Camry", 2020, 4)
moto1 = Motorcycle("Harley-Davidson", "Street 750", 2019, 750)

print(car1.get_info())
print(car1.start())
print(car1.drive(50))
print(car1.refuel(20))

print("\n" + moto1.get_info())
print(moto1.start())
print(moto1.wheelie())


print("\n2 Тест BankAccount:")
account = BankAccount("Іван Петренко", "4149625812349876", 5000)
print(f"Власник: {account.owner}")
print(f"Картка: {account.get_masked_card()}")
print(account.deposit(2000))
print(account.withdraw(1500, "1234"))
print(account.get_balance("1234"))

print("\n3 Тест Animal (Поліморфізм):")
dog = Dog("Рекс")
cat = Cat("Мурка")
bird = Bird("Кеша")

animals = [dog, cat, bird]
animal_show(animals)


print("\n4 Тест Student:")
student1 = Student("Олександр Коваленко", "KN2301", "КН-23")
student2 = Student("Марія Шевченко", "KN2302", "КН-23")

print(student1.add_grade("Програмування", 95))
print(student1.add_grade("Математика", 88))
print(student1.add_grade("Англійська", 92))

print(student2.add_grade("Програмування", 78))
print(student2.add_grade("Математика", 85))

print("\n" + student1.get_info())
print(student2.get_info())
print("\n" + Student.get_student_count())

print("\n" + "=" * 50)
print("✓ Всі тести пройдено успішно!")
print("=" * 50)
