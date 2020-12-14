"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'Машина повернула на лево')
        elif direction == 'right':
            print(f'Машина повернула на право')
        else:
            print(f'Машина куда-то повернула :))')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина превысила скорость на: {self.speed - 60}')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина превысила скорость на: {self.speed - 40}')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class PoliceCar(Car):
    pass


town_car_45 = TownCar(45, "yellow", "man")
print(town_car_45.color)
print(town_car_45.name)
town_car_45.turn("left")
town_car_45.show_speed()

town_car_70 = TownCar(70, "green", "hyundai")
print(town_car_70.color)
print(town_car_70.name)
town_car_70.turn("right")
town_car_70.show_speed()

sport_car = SportCar(270, "red", "McLaren")
print(sport_car.color)
print(sport_car.name)
sport_car.turn("right")
sport_car.show_speed()

work_car_35 = WorkCar(35, "white", "bobcat")
work_car_35.show_speed()

work_car_45 = WorkCar(45, "white", "bobcat")
work_car_45.show_speed()

police_car = PoliceCar(170, "black", "ford", True)
print(police_car.is_police)
