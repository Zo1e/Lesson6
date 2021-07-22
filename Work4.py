class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')


    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def turn_left(self):
        print(f'{self.name} повернула налево')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Towncar {self.name} едет со скоростью {self.speed}')

        if self.speed > 40:
            print(f'Скорость Towncar {self.name} превышена')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Towncar {self.name} едет со скоростью {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Workcar {self.name} едет со скоростью {self.speed}')

        if self.speed > 60:
            print(f'Скорость Workcar {self.name} превышена')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Towncar {self.name} едет со скоростью {self.speed}')

    def police(self):
        print(f'Police car {self.name} едет со включенными мигалками, всем прижаться к обочине!')

    def what(self):
        if self.is_police == True:
            print(f'{self.name} - полицейская машина')
        else:
            print(f'{self.name} не полицейская машина, езжайте спокойно')



toyota = SportCar(80, 'Зелёный', 'Toyota', True)
mercedes = TownCar(100, 'Красный', 'Mercedes', False)
zaz = WorkCar(50, 'Жёлтый', 'Zaz', False)
ferrari = PoliceCar(150, 'Фиолетовый',  'Ferrari', True)
print(zaz.turn_left())
print(f'Когда {mercedes.turn_right()}, {toyota.stop()}')
print(f'{zaz.go()} со скоростью {zaz.show_speed()}')
print(f'Цвет {zaz.name} - {zaz.color}')
print(f'{toyota.name} Полицейская машина? {toyota.is_police}')
print(f'{zaz.name} Полицейская машина? {zaz.is_police}')
print(toyota.show_speed())
print(mercedes.show_speed())
print(ferrari.police())
print(ferrari.show_speed())



