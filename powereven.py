from functools import reduce


if __name__ == "__main__":
    source = [el for el in range(100, 1001) if el % 2 == 0]
    result = reduce(lambda x, y: x*y, source)
    print(f'Source: {source}\nResult: {result}')
