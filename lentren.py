from argparse import ArgumentParser
from typing import Tuple


UTILITE_DESCRIPTION = """Necessary training period calculator.
This program is calculator for runners that want to know when they achieve target result. 
Basically you have to specify your initial result and your target in km. Default growth value is 10%.
Returned value is the days count that you need to achieve your target."""


argparser = ArgumentParser(description=UTILITE_DESCRIPTION)
argparser.add_argument('initial_result', type=float, help='your initial result in km')
argparser.add_argument('target', type=float, help='result that you want to achieve in km')
argparser.add_argument('-g', '--growth', type=int, default=10, required=False,
                       help='your growth per training in percents')
argparser.add_argument('-v', '--verbose', action='store_true', help='flag to show advanced information')


def calc_daily_result(initial_result: float, growth: int, target: float) -> Tuple[int, float]:
    current_result = initial_result
    current_day = 0
    growth = 1 + growth/100
    while current_result < target:
        current_result *= growth
        current_day += 1
        yield current_day, round(current_result, 3)


def run(initial_result: float, growth: int, target: float, verbose: bool):
    for day, result in calc_daily_result(initial_result, growth, target):
        if verbose:
            print(f'Day {day} result: {result}km.')
    message = f'Probably you achieve the target at the {day} day with result: {result}km' if verbose else day
    print(message)


if __name__ == '__main__':
    args = argparser.parse_args()
    run(args.initial_result, args.growth, args.target, args.verbose)
