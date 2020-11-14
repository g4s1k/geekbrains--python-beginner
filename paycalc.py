from argparse import ArgumentParser


DESCRIPTION = """This program calculate employee salary. Just set hours, tax and bonus. Formula is hours*tax*(1 + bonus/100)."""


def calc_pay(hours: float, tax: float, bonus: float) -> float:
    return hours*tax*(1 + bonus/100)


argparser = ArgumentParser(description=DESCRIPTION)
argparser.add_argument('hours', type=float,
                       help='Hours amount that the employee did work')
argparser.add_argument('tax', type=float, help='Payment per one hour')
argparser.add_argument('bonus', type=float, help='Relative bonus in percents')


if __name__ == "__main__":
    args = argparser.parse_args()
    payment = calc_pay(args.hours, args.tax, args.bonus)
    print(payment)
