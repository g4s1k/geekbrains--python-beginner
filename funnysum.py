from typing import Tuple


def numbers_generator(n_times: int, number: str) -> Tuple[int, str]:
    for iteration in range(n_times):
        yield iteration, number*(iteration + 1)


def funny_sum_calc(n_times: int, number: str) -> str:
    res = 0
    for i, val in numbers_generator(n_times, number):
        res += int(val)
        if not i:
            formula = val
            continue
        formula += f' + {val}'
    result = f'{formula} = {res}'
    return result


if __name__ == '__main__':
    print("Hello, user! I'm Funny Sum.\n")
    print('--------------------------------------------------\n')
    n_times = int(input('Please input iterations count: '))
    number = input('Now enter some number: ')
    print('\n', funny_sum_calc(n_times, number))
