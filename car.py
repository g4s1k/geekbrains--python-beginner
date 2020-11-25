class Car:
    __state = 'stay'
    __direction = 'forward'
    __directions = ['back', 'left', 'forward', 'right']
    __speed = 0

    def __init__(self, max_speed: float, color: str, name: str, is_police: bool):
        self.color = color
        self.name = name
        self.__is_police = is_police
        self.__max_speed = max_speed

    def go(self, speed: float):
        if speed <= 0:
            raise ValueError(
                'Speed value must be positive!\nTo stop car use method "stop".\nTo move back use method "go_back" or turn car around.')
        self.__state = 'moving'
        if speed <= self.__max_speed:
            self.__speed = speed
        else:
            self.__speed = self.__max_speed

    def stop(self):
        self.__state = 'stay'
        self.__speed = 0

    def go_back(self):
        if self.__speed > 0:
            raise RuntimeWarning(
                'You can\'t go back when you moving forvard. Previously you should start moving.')
        self.__state = 'moving'
        self.__speed = -5

    def turn(self, direction: str):
        if direction not in self.__directions:
            raise ValueError(
                f'Direction must be one of {self.__directions}, got {direction}')
        if self.__speed == 0:
            raise RuntimeWarning(
                'You can\'t turn car when it stay. Previously you should start moving.')
        self.__direction = direction

    @property
    def movement_state(self):
        description = f'{self.color.capitalize()} {self.name} {self.__state}'
        direction = '' if self.__state == 'stay' else f' turned {self.__direction}'
        report = f'{description}{direction}.\nCurrent speed is {self.__speed} km/h.'
        return report


class TownCar(Car):
    _speed_limit = 60
    _name = 'town car'

    def __init__(self, color: str):
        super().__init__(max_speed=160, color=color, name=self._name, is_police=False)

    @property
    def movement_state(self):
        report = super().movement_state
        alert = f'You exceeded the speed limit!' if self._Car__speed > self._speed_limit else ''
        return report + alert


class WorkCar(TownCar):
    _speed_limit = 40
    _name = 'work car'


class SportCar(Car):
    _name = 'sport car'

    def __init__(self, color: str):
        super().__init__(max_speed=240, color=color, name=self._name, is_police=False)


class PoliceCar(Car):
    _name = 'police car'

    def __init__(self):
        super().__init__(max_speed=240, color='black', name=self._name, is_police=False)


if __name__ == "__main__":
    car = TownCar('red')
    print(car.movement_state)
    car.go(80)
    car.turn('right')
    print(car.movement_state)
    car.turn('left')
    car.stop()
    print('----------------------------------------')
    car = WorkCar('yellow')
    print(car.movement_state)
    car.go(30)
    car.turn('back')
    print(car.movement_state)
    car.stop()
