class Road:
    __asphalt_density = 2480

    def __init__(self, width: float, lenght: float):
        self.__width = width
        self.__lenght = lenght

    def set_density(self, density: float):
        self.__asphalt_density = density

    def calc_asphalt_mass(self, thickness: int = 100):
        asphalt_volume = self.__width*self.__lenght*thickness
        return asphalt_volume*self.__asphalt_density


if __name__ == "__main__":
    road_width = input('Please input average road width in meters: ')
    road_lenght = input('Please input road lenght in km\'s: ')
    thickness = input(
        'Please input average asphalt thickness in millimeters: ')
    road = Road(float(road_width), float(road_lenght))
    asphalt_mass = road.calc_asphalt_mass(int(thickness))
    print(
        f'You need about {asphalt_mass*10**-3:.2f} tons of asphalt to construct the road.')
