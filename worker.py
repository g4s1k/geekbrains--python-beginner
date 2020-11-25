class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Engineer(Worker):
    def __init__(self, name: str, surname: str, wage: float, bonus: float):
        super().__init__(name, surname, 'engineer', wage, bonus)

    @property
    def full_name(self):
        return f'{self.surname} {self.name}'

    @property
    def total_income(self):
        return sum(self._Worker__income.values())


if __name__ == "__main__":
    name, surname = input('Please enter workers name and surname: ').split()
    wage = float(input('Please enter workwrs wage: '))
    bonus = float(input('Please enter workwrs bonus: '))
    engineer = Engineer(name, surname, wage, bonus)
    print('--------------------------------------------')
    print(f'Information about {engineer.position} {engineer.full_name}')
    print(f'Monthly income: {engineer.total_income} rub')
