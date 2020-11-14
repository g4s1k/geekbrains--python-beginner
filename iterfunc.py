from itertools import cycle, count
from random import randint
from typing import Callable


def randomstop(*args, iterator: Callable, coin: int = 42):
    for element in iterator(*args):
        if randint(0, coin) == coin//2:
            return
        yield element


if __name__ == "__main__":
    try:
        seq = [el/randint(3, 5) for el in randomstop(0, 2, iterator=count)]
        for el2 in randomstop(seq, iterator=cycle):
            print(el2)
    except KeyboardInterrupt:
        pass
