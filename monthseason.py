from argparse import ArgumentParser


DESCRIPTION = """Use this utilite to receive season name from month number."""
SEASONS = ['winter', 'spring', 'summer', 'authumn']
SEASONS_DICT = dict(
    zip(range(12),
        sum([[month for _ in range(3)] for month in SEASONS], []))  # Отступ - баг линтера
)


def get_season(month: int, use_dict: bool = False) -> str:
    if not month or month > 12:
        raise ValueError(
            f'Month number should be between 1 and 12, got {month}')
    month = month if month < 12 else 0
    if use_dict:
        return SEASONS_DICT[month]
    else:
        index = month//3
        return SEASONS[index]


argparser = ArgumentParser(description=DESCRIPTION)
argparser.add_argument('month', type=int, help='Month number 1..12')
argparser.add_argument('-d', '--use_dict', action='store_true',
                       help='Set this flag to use dict as a source')


if __name__ == "__main__":
    args = argparser.parse_args()
    month = args.month
    use_dict = args.use_dict
    season = get_season(month, use_dict=use_dict)
    print(season)
