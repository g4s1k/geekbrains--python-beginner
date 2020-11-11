def clear_word(word: str) -> str:
    for char in word:
        char_pos = ord(char)
        if (char_pos >= 65 and char_pos <= 90) or (char_pos >= 97 and char_pos <= 122):
            continue
        word = word.replace(char, '')
    return word


def custom_capitalize(word: str) -> str:
    word = clear_word(word)
    return word.capitalize()


if __name__ == "__main__":
    user_input = input('Enter some sentence: \n')
    words = user_input.split()
    result = [custom_capitalize(word) for word in words]
    print('Result: \n', ' '.join(result))
