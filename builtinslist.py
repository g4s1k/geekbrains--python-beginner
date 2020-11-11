builtins_list = [1, 1.1, complex(0, 4), 'None', None, {}, [
], ('a', 'b'), set(), ValueError('missed value'), frozenset(), b'10']


if __name__ == '__main__':
    print('builtinslist: ', builtins_list)
    print('types contained: ')
    for el in builtins_list:
        print(type(el), el)
