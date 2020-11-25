from typing import Union
from time import sleep
from itertools import cycle


class Timing(dict):
    __keys_template = ['green', 'red', 'yellow']
    __structure_error_help = """Timing object should be a dict looks like {'red': 7, 'yellow': 2, 'green': 14}"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.__keys_template:
            if key not in self:
                raise ValueError(self.__structure_error_help)
            val = self[key]
            if not isinstance(val, int):
                raise ValueError('Timing values should be integers')


class TrafficLight:

    __color = 'yellow'  # turned off traffic light usual blinkins yellow

    def __init__(self, timing: Union[Timing, dict] = Timing(red=7, yellow=2, green=10)):
        if isinstance(timing, dict):
            timing = Timing(**timing)
        self.timing = timing
        self.__colors_sequence = cycle(
            ['green', 'yellow', 'red'])  # real world order

    def next(self):
        self.__color = next(self.__colors_sequence)

    def show_color(self):
        print(self.__color)

    def run(self):
        print('Traffic light started.\nPress ctrl + C to stop TrafficLight')
        try:
            while True:
                sleep(self.timing[self.__color])
                self.next()
                self.show_color()
        except KeyboardInterrupt:
            while not self.__color == 'yellow':  # turned off traffic light usual blinkins yellow
                self.next()
            print('Traffic light stopped')
            self.show_color()


if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.show_color()  # show state before turn it on
    traffic_light.run()
