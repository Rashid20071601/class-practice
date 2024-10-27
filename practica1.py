# Задача 1: Инкапсуляция
# Создай класс Employee с приватными атрибутами name, position и salary. Реализуй методы для установки и получения этих значений:
#
# 1 - Метод set_salary(self, amount) должен проверять, что amount больше нуля, и устанавливать зарплату.
# 2 - Метод get_salary(self) должен возвращать текущую зарплату.
# 3 - Добавь метод increase_salary(self, percent) для увеличения зарплаты на указанный процент.
#
# Задание:
# 1 - Создай объект класса Employee с начальными значениями имени и должности.
# 2 - Попробуй изменить зарплату через метод и вывести новую зарплату.
# 3 - Увеличь зарплату на 10% и выведи результат.

class Employee:
    def __init__(self, name, position, salary = 0):
        self.name = name
        self.position = position
        self.__salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"Зарплата была увеличена на {amount}. Текущая зарплата: {self.__salary}")
        else:
            print("Сумма к зарплате должно быть положительным числом!")
            exit()

    def get_salary(self):
        return self.__salary

    def increase_salary(self):
        perc = int(input("На сколько процентов увеличить зарплату?: "))
        if 0 < perc <= 100:
            self.__salary = self.__salary * (perc / 100) + self.__salary

artem = Employee('Artem', 'Junior')
artem.set_salary(100000)
print(artem.get_salary())
artem.increase_salary()
print(artem.get_salary())

print("------------------------------------------------------------------------------")

# Задача 2: Полиморфизм
# Создай три класса Vehicle (базовый класс), Car и Bike (наследуют от Vehicle). Каждый класс должен иметь метод move(self), который выводит разное сообщение в зависимости от типа транспортного средства.
#
# 1 - В классе Vehicle метод move может выводить что-то вроде "The vehicle is moving".
# 2 - В классе Car метод move должен выводить "The car is driving on the road".
# 3 - В классе Bike метод move должен выводить "The bike is pedaling on the path".
#
# Задание:
# 1 - Создай функцию start_trip(vehicle) которая принимает объект класса Vehicle и вызывает метод move.
# 2 - Создай объекты классов Car и Bike и вызови для каждого функцию start_trip.

class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road")

class Bike(Vehicle):
    def move(self):
        print("The bike is pedaling on the path")

def start_trip(vehicle):
    vehicle.move()

car = Car()
bike = Bike()
start_trip(car)
start_trip(bike)


print("------------------------------------------------------------------------------")


# Задача 3: Статические методы и методы класса
# Создай класс Circle, который будет иметь:
#
# Обычный метод area, вычисляющий площадь круга.
# Статический метод pi, который возвращает значение числа Пи (например, 3.14159).
# Метод класса from_diameter, который принимает диаметр круга и возвращает объект класса, у которого радиус равен половине диаметра.
#
# Задание:
# Создай объект класса Circle с радиусом.
# Используй метод area для вычисления площади круга.
# Создай объект с помощью метода класса from_diameter.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_circle = math.pi * self.radius ** 2
        return f"{area_circle:.2f}"

    @staticmethod
    def pi():
        return f"{math.pi:.1f}"

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)  # Возвращаем объект класса с вычисленным радиусом


circle = Circle(5)
print(circle.area())
print(circle.from_diameter(10).radius)


print("------------------------------------------------------------------------------")


