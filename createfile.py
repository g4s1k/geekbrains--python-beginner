from setup import path, FILE_NAME


if __name__ == "__main__":
    print(
        f'Writing into {FILE_NAME} started, to exit please enter empty line.')
    with open(path, 'w', encoding='utf-8') as f:
        while True:
            line = input('Please enter line to write: ')
            if line:
                f.write(line + '\n')
            else:
                break
