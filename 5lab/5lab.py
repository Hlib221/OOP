import random


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "Insufficient funds"

    def get_balance(self):
        return self.__balance


account = BankAccount("Bohdan", 1000)

for i in range(10):
    action = random.choice(["deposit", "withdraw"])
    amount = round(random.uniform(50, 300), 2)

    if action == "deposit":
        account.deposit(amount)
        print(f"Ітерація {i + 1}: поповнення на {amount:.2f}, баланс: {account.get_balance():.2f}")
    else:
        result = account.withdraw(amount)
        if isinstance(result, str):
            print(f"Ітерація {i + 1}: спроба зняти {amount:.2f} — {result}, баланс: {account.get_balance():.2f}")
        else:
            print(f"Ітерація {i + 1}: зняття {amount:.2f}, баланс: {account.get_balance():.2f}")

print(f"\nКінцевий баланс: {account.get_balance():.2f}")

print("-" * 50)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

    def vehicle_type(self):
        return f"Тип транспорту: наземний"


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"


car = Car("Toyota", "Camry", 5)
print(car.display_info())
print(car.vehicle_type())

print("_" * 50)

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Fish(Animal):
    pass


animals = [Dog(), Cat(), Fish()]
for animal in animals:
    result = animal.speak()
    print(f"{animal.__class__.__name__}: {result}")
    
print("_" * 50)

from abc import ABC, abstractmethod
from random import randint, choice


class Item(ABC):
    def __init__(self, name, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass


class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"Завдаємо удару мечем {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишилось здоров'я: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака меча {self.name}: {self.__attack_power + self._sharp} одиниць"

    def sharpening(self):
        self._sharp += 1


class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item):
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"Завдаємо удару сокирою {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишилось здоров'я: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака сокири {self.name}: {self.__attack_power + self._sharp} одиниць"

    def sharpening(self):
        self._sharp += 1


class Bow(Item):
    def __init__(self, name, attack_power: int, range_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another_item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return f"Випускаємо стрілу з {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишилось здоров'я: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака лука {self.name}: {self.__attack_power + self.range_power} одиниць"

    def reload(self):
        self.range_power += 1


def get_buff_action(weapon):
    if isinstance(weapon, Bow):
        return "reload"
    return "sharpening"


def apply_buff(weapon):
    if isinstance(weapon, Bow):
        weapon.reload()
        print(f"  Перезарядка! Дальність тепер: {weapon.range_power}")
    else:
        weapon.sharpening()
        print(f"  Заточка! {weapon.get_attack_power}")


def choose_weapon():
    weapons = [
        Sword("Ескалібур", 100),
        Axe("Кратос", 95),
        Bow("Леґолас", 85, 10),
    ]
    chosen = choice(weapons)
    print(f"Тобі випала зброя: {chosen.__class__.__name__} — {chosen.name}")
    return chosen


print("ПОКРОКОВА БОЙ-СИМУЛЯЦІЯ")

player = choose_weapon()
enemy = choice([
    Sword("Темний лицар", 90),
    Axe("Орк", 85),
    Bow("Ельф", 80, 8),
])
print(f"Ворог: {enemy.__class__.__name__} — {enemy.name}")

buff_label = "reload (дальність +1)" if isinstance(player, Bow) else "sharpening (заточка)"

step = 1
while player.health > 0 and enemy.health > 0:
    print(f"\nХід {step}")
    print(f"  Твоє здоров'я: {player.health} | Здоров'я ворога: {enemy.health}")
    print(f"  Дії: [1] attack  [2] {buff_label}")

    action = input("  Твій вибір (1/2): ").strip()

    if action == "1":
        print(" ", player.attack(enemy))
    elif action == "2":
        apply_buff(player)
    else:
        print("  Невірна дія, хід пропущено.")

    if enemy.health <= 0:
        print(f"\nПеремога за {player.name}!")
        break

    print(" ", enemy.attack(player))

    if player.health <= 0:
        print(f"\nПеремога за {enemy.name}!")
        break

    step += 1

print("_" * 50)