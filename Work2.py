class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def craft(self,  _mass, _thickness):
        self._mass = _mass
        self._thickness = _thickness
        Ready_road = self._length * self._width * self._mass * self._thickness
        print(f'Необходимая масса асфальта - {Ready_road} т.')

new_road = Road(3000, 10)
new_road.craft(25, 5)


