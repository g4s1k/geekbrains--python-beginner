def find_max_digit(number: int) -> int:
    result = 0
    while number:
        digit = number % 10
        number = number // 10
        result = digit if digit > result else result
    return result


if __name__ == '__main__':
    print("Hello, user! I'm Max Digit.\n")
    print('--------------------------------------------------\n')
    number = int(input('Please input some number: '))
    print('\nMax digit in this number is: ', find_max_digit(number))
