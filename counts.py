from setup import path, FILE_NAME


if __name__ == "__main__":
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines_count = len(lines)
    words_count = [len(line.split()) for line in lines]
    print(f'Lines count in {FILE_NAME} is {lines_count}')
    print(f'Words counts: {words_count}')
