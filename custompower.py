from typing import Union


def custom_power(x: float, y: int) -> Union[float, str]:
    if x == 0:
        result = 0 if y else 'undefiniteness'
        return result
    result = 1.0
    mult = x if y > 0 else 1/x
    for _ in range(abs(y)):
        result *= mult
    return result


if __name__ == "__main__":
    x = float(input('Please enter some positive float number x: '))
    y = int(input('Please enter some negative integer y: '))
    if y >= 0 or x <= 0:
        raise ValueError(
            f'x should be positive float and y - negative int, got x={x}, y={y}.')
    print(f'{x}e{y} = ', round(custom_power(x, y), 3))
