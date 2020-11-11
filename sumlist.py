from typing import Union


class ListSummator:
    def __init__(self, stopper: str = '!q', sep: str = ' '):
        self._cache = 0
        self._status = 'active'
        self._stopper = stopper
        self._sep = sep

    @staticmethod
    def parse_string(string: str, sep: str = ' ') -> list:
        return string.split(sep)

    def add_elements(self, elements: Union[list, str]):
        if isinstance(elements, str):
            elements = self.parse_string(elements, self._sep)
        for element in elements:
            if element == self._stopper:
                self._status = 'stopped'
                break
            self._cache += float(element)

    def show_summ(self) -> float:
        return self._cache

    def set_stopper(self, stopper: str):
        self._stopper = stopper

    def set_separator(self, sep: str):
        self._sep = sep

    def get_status(self):
        return self._status

    def reset(self):
        self._cache = 0
        self._status = 'active'


if __name__ == "__main__":
    print('Test for list summator. Default stop sequence is "!q", default separator is whitespace.')
    summator = ListSummator()
    actions = {'set_stopper':
               ('Please enter stop symbhols sequence or "cancel" to scip: ',
                summator.set_stopper),
               'set_separator':
               ('Please enter new separator or "cancel" to scip: ',
                summator.set_separator),
               'reset':
               ('Done. Press enter to continue.',
                lambda x: summator.reset())
               }
    while True:
        user_input = input(
            'Please set action or enter numbers sequence. Available actions: set_stopper, set_separator, reset\n')
        action = actions.get(user_input)
        if action:
            message = action[0]
            func = action[1]
            new_value = input(message)
            if new_value != 'cancel':
                func(new_value)
            continue
        else:
            summator.add_elements(user_input)
            print('Current sum is: ', summator.show_summ())
        if summator.get_status() == 'stopped':
            break
