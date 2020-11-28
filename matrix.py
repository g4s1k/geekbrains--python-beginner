from typing import List, Union
from random import randint


class DigitalMatrix:
    pass


class Matrix(DigitalMatrix):
    def __init__(self, massive: List[List[Union[int, float]]]):
        rows_count = len(massive)
        cols_count = max([len(row) for row in massive])
        self.__shape = [rows_count, cols_count]
        self.__rows = []
        self.__min = self.__max = massive[0][0]
        for row in massive:
            for el in row:
                if el > self.__max:
                    self.__max = el
                if el < self.__min:
                    self.__min = el
            while len(row) < cols_count:
                row.append(0)
            self.__rows.append(row)

    @property
    def shape(self):
        return tuple(self.__shape)

    @property
    def max(self):
        return self.__max

    @property
    def min(self):
        return self.__min

    def __str__(self):
        max_len = max((len(str(self.min)), len(str(self.max))))
        text_rows = []
        for row in self.__rows:
            text_row = []
            for el in row:
                text_el = str(el)
                while len(text_el) < max_len:
                    text_el = ' ' + text_el
                text_row.append(text_el)
            text_row = '\t'.join(text_row)
            text_rows.append(text_row)
        text = '\n'.join(text_rows)
        return text

    @property
    def rows(self):
        return list(self.__rows)

    def append_row(self, row: List[Union[int, float]]):
        while len(row) < self.shape[1]:
            row.append(0)
        self.__rows.append(row)
        self.__shape[0] += 1

    def append_column(self, column: List[Union[int, float]]):
        while len(column) < self.shape[0]:
            column.append(0)
        for row, new_el in zip(self.__rows, column):
            row.append(new_el)
        self.__shape[1] += 1

    def __add__(self, other: DigitalMatrix):
        rows_count, cols_count = [max(el)
                                  for el in zip(self.shape, other.shape)]
        result = [[] for _ in range(rows_count)]
        for i in range(rows_count):
            for j in range(cols_count):
                x1 = self.__rows[i][j] if self.shape[0] > i and self.shape[1] > j else 0
                x2 = other._Matrix__rows[i][j] if other.shape[0] > i and other.shape[1] > j else 0
                result[i].append(x1 + x2)
        return Matrix(result)


if __name__ == "__main__":
    m1 = Matrix([[randint(-10, 10) for j in range(4)] for i in range(4)])
    m2 = Matrix([[randint(-7, 13) for j in range(3)] for i in range(3)])
    m3 = m1 + m2
    print(m1)
    print('PLUS')
    print(m2)
    print('IS EQUAL TO')
    print(m3)
