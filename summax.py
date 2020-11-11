def sum_max(*args):
    sorted_args = sorted(args)
    return sum(sorted_args[-2:])


if __name__ == "__main__":
    print('Please enter comma separated digits list (For example: "1, 2, 3"):')
    str_input = input()
    digits = [float(x) for x in str_input.split(', ')]
    print('Summ two maximal elements equal: ', sum_max(*digits))
