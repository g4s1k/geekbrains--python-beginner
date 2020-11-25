class Stationery:
    title = 'stationery'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = 'pen'

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    name = 'pencil'

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    name = 'handle'

    def draw(self):
        print('Рисуем маркером')


if __name__ == "__main__":
    stationery = Stationery()
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    stationery.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
