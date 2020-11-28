from abc import ABC, abstractproperty
from typing import List


class Clothes(ABC):
    size: int
    name: str

    @abstractproperty
    def fabric_count(self) -> float:
        pass


class Coat(Clothes):
    def __init__(self, size: float, name=''):
        self.size = size
        self.name = name

    @property
    def fabric_count(self):
        return self.size/6.5 + 0.5


class BusinessSuit(Clothes):
    def __init__(self, size: float, name=''):
        self.size = size
        self.name = name

    @property
    def fabric_count(self):
        return self.size*2 + 0.3


class ClothesParty:
    choose = {'coat': Coat, 'suit': BusinessSuit}

    def __init__(self, clothes_type: str, count: int, size: float, name: str):
        cls = self.choose.get(clothes_type)
        if not cls:
            raise ValueError(
                f'"coat" and "suit" clothes types are available now, not a {clothes_type}')
        self.clothes_type = clothes_type
        self.party_size = count
        self.unit_size = size
        self.party_name = name
        self.sample = cls(size, name)
        self.fabric_per_clothes = cls(size).fabric_count

    @property
    def fabric_count(self):
        return self.fabric_per_clothes*self.party_size*1.1


class ClothesLine:
    def __init__(self, batches: List[ClothesParty] = []):
        self.batches = batches

    def add_party(self, party: ClothesParty):
        self.batches.append(party)

    @property
    def fabric_count(self):
        return sum([party.fabric_count for party in self.batches])


if __name__ == "__main__":
    print('Fabric count calculator. Pess Ctrl + C to stop')
    print('---------------------------------------------------------------------------')
    iteration = 1
    clothes_line = ClothesLine()
    try:
        while True:
            print(f'Party {iteration} parameters.')
            clothes_type = input(
                'Please enter clothes type (coat and suit are available now): ')
            size = float(input('Please enter size: '))
            count = int(input('Please enter count: '))
            name = input('Please enter the party name: ')
            party = ClothesParty(clothes_type, count, size, name)
            print(
                f'Fabric count that you need to produce this clothes party: {party.fabric_count}')
            clothes_line.add_party(party)
            iteration += 1
            print(
                '---------------------------------------------------------------------------')
    except KeyboardInterrupt:
        print(
            '\n---------------------------------------------------------------------------')
        print(f'Summary fabric count is: {clothes_line.fabric_count}')
