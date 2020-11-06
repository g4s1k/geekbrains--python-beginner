class ProfitCalculator:
    def __init__(self, profit: float, costs: float, employees_count: int = 1):
        self.profit = profit
        self.costs = costs
        self.employees = employees_count

    def get_profit_status(self) -> str:
        result = 'profitable'
        if self.profit <= self.costs:
            result = 'unprofitable'
        return result

    def calc_profitability(self) -> float:
        result = self.profit/self.costs
        return round(result, 3)

    def calc_profit_per_employee(self) -> float:
        result = self.profit/self.employees
        return round(result, 2)


if __name__ == '__main__':
    print("Hello, user! I'm Profit Calculator.\n")
    print('--------------------------------------------------\n')
    print('Please input parameters:')
    profit = float(input('Profit: '))
    costs = float(input('Costs: '))
    employees_count = int(input('Employees count: '))
    profit_calculator = ProfitCalculator(profit=profit, costs=costs, employees_count=employees_count)
    print('--------------------------------------------------\n')
    print('Calculations result:')
    print(f'\tis profitable: {profit_calculator.get_profit_status()}')
    print(f'\tprofitability: {profit_calculator.calc_profitability()}')
    print(f'\tprofit per employee: {profit_calculator.calc_profit_per_employee()}')
