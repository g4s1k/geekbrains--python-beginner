class _Rating:
    pass


class Rating(_Rating):
    def __init__(self):
        self.__rating = []
        self.__shape = 0

    @staticmethod
    def _sort_elements(group: list) -> list:
        group_len = len(group)
        for i in range(group_len - 1, 0, -1):
            pos_x = i
            pos_y = i - 1
            x = group[pos_x]
            y = group[pos_y]
            if x > y:
                group[pos_y] = x
                group[pos_x] = y
        return group

    def add_element(self, element: int):
        self.__rating.append(element)
        self.__shape += 1
        if self.__shape == 1:
            return
        self.__rating = self._sort_elements(self.__rating)

    def add_group(self, group: list):
        for element in group:
            self.add_element(element)

    def show_rating(self) -> str:
        return self.__rating.__repr__()

    @classmethod
    def from_list(cls, int_list: list) -> _Rating:
        rating = cls()
        rating.add_group(int_list)
        return rating


if __name__ == "__main__":
    rating = Rating.from_list([5, 7, 10, 3, 8])
    print('Current rating is: ', rating.show_rating())
    print('------------------------------------------------------')
    while True:
        element = input('Please add element or type "done" to exit: ')
        if element.lower() == 'done':
            print('------------------------------------------------------')
            print('Final rating is: ', rating.show_rating())
            print('------------------------------------------------------')
            break
        else:
            element = int(element)
            rating.add_element(element)
            print('Current rating is: ', rating.show_rating())
            print('------------------------------------------------------')
