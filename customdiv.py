from typing import Union


def custom_div(a: Union[int, float], b: Union[int, float]) -> Union[float, str, None]:
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        if a == 0:
            print('0/0 is undefiniteness!')
            return
        elif a > 0:
            return 'inf'
        else:
            return '-inf'


if __name__ == "__main__":
    print('Custom division function testing.')
    a = float(input('Please enter numerator: '))
    b = float(input('Please enter denominator: '))
    print('Result: ', custom_div(a, b))
