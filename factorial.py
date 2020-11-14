def calc_factorial(num: int) -> int:
    result = 1
    for mult in range(num + 1):
        if mult > 1:
            result *= mult
        yield result


if __name__ == "__main__":
    num = int(input('Введите целое неотрицательное число: '))
    if num < 0:
        raise ValueError('Введено отрицательное число')
    for result in calc_factorial(num):
        print(result)
