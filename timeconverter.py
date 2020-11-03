from datetime import time


def convert_time(seconds: int) -> str:
    hours = seconds // 3600
    minutes = seconds // 60 - hours * 60
    seconds_tail = seconds % 60
    try:
        calculated_time = time(hour=hours, minute=minutes, second=seconds_tail)
        return calculated_time.isoformat()
    except ValueError:
        return 'Probably value is too large!'


if __name__ == '__main__':
    print("--------------------------------------------------\n"
          "Hello, user! I'm Time Converter.\n"
          "I can convert time value in seconds to ISO format!\n"
          "TO EXIT just type 'exit' word and press ENTER.")
    seconds = ''
    while True:
        seconds = input('\n--------------------------------------------------\n'
                        'Please input time in seconds: ')
        if seconds.lower() == 'exit':
            break
        if seconds:
            seconds = int(seconds)
            print(f'Convertation result: {convert_time(seconds)}')
        else:
            print('Seems entered value is empty!')
