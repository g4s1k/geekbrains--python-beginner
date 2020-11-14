from random import randint


if __name__ == "__main__":
    original_list = [randint(0, 10) for _ in range(randint(15, 25))]
    uniq_elements = [el for index, el in enumerate(
        original_list) if el not in original_list[:index]]
    print(
        f'Original list: {original_list} \nUnique elements: {uniq_elements}')
