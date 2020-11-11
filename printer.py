def printer(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    print('Please input user info as key-value pairs. For example: "name: Ivan". Type "done" to finish.')
    user_attrs = {}
    while True:
        try:
            str_attr = input()
            if str_attr.lower() == 'done':
                break
            key, value = str_attr.split(': ')
            user_attrs[key] = value
        except KeyboardInterrupt:
            break
    printer(**user_attrs)
