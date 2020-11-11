if __name__ == "__main__":
    print('Please input several words splitted by whitespaces: ')
    str_sequence = input()
    print('----------------------------------------------------')
    sequence = str_sequence.split(' ')
    for word in sequence:
        print(word[:10])
