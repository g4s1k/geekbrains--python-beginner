def pairs_flipper(sequence: list) -> list:
    limit = len(sequence)
    last = sequence.pop() if limit % 2 > 0 else None
    result = []
    for i in range(0, limit, 2):
        result += reversed(sequence[(i):(i+2)])
    if last is not None:
        result.append(last)
    return result


if __name__ == '__main__':
    print('This script flip pairs of list elements. You should input some list.'
          'Use such pattern please: a, b, c, d')
    print('---------------------------------------------------------------------')
    str_sequence = input('Please input some list: ')
    sequence = str_sequence.split(', ')
    result = pairs_flipper(sequence)
    print('---------------------------------------------------------------------')
    print('Result: ', result)
