def decode_lines(lines: list) -> dict:
    items = [line.split() for line in lines]
    result = {name: float(salary) for name, salary in items}
    return result


def get_poors(salaries: dict, threshold: float = 20000.0) -> list:
    result = []
    for name in salaries:
        salary = salaries[name]
        if salary < threshold:
            result.append(name)
    return result


def get_average(salaries: dict) -> float:
    salary_values = list(salaries.values())
    result = sum(salary_values)/len(salary_values)
    return result


if __name__ == "__main__":
    with open('./salary.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    salaries = decode_lines(lines)
    print('Persons with weak salary: ')
    for poor in get_poors(salaries):
        print(poor)
    print(f'Average empoyees salary: {get_average(salaries)}')
