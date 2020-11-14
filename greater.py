from random import randint
from typing import List


def get_greater_element(sequence: List[int]) -> int:
    for i in range(len(sequence) - 1):
        first_el = sequence[i]
        second_el = sequence[i+1]
        if second_el > first_el:
            yield second_el


def get_greater_element2(sequence: List[int]) -> List[int]:
    result = [el2 for el1, el2 in zip(
        original_list[:-1], original_list[1:]) if el2 > el1]
    return result


def get_greater_element3(sequence: List[int]) -> List[int]:
    result = [el for index, el in enumerate(
        original_list[1:]) if el > original_list[index]]
    return result


if __name__ == "__main__":
    original_list = [randint(0, 100) for _ in range(randint(5, 20))]
    modified_list = [el for el in get_greater_element(original_list)]
    modified_list2 = get_greater_element2(original_list)
    modified_list3 = get_greater_element3(original_list)
    print(
        f'Original list: {original_list} \n'
        f'Modified list: {modified_list}\n'
        f'Modified list 2: {modified_list2}\n'
        f'Modified list 3: {modified_list3}')
