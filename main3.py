# Доработайте класс прямоугольник из прошлых семинаров. Добавьте возможность изменять длину и ширину 
# прямоугольника и встройте контроль недопустимых значений (отрицательных). Используйте декораторы свойств.

class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self._width = length
        else:
            self._width = width
        self._length = length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
        else:
            raise ValueError('Не правильный аргумент')

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
        else:
            raise ValueError('Не правильный аргумент')

    def get_perimetr(self):
        return 2 * self._length + 2 * self._width

    def get_area(self):
        return self._length * self._width

    def __add__(self, other):
        width = self._width
        perimetr = self.get_perimetr() + other.get_perimetr()
        length = (perimetr - 2 * width) / 2
        return Rectangle(width, length)

    def __sub__(self, other):
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        length = int(perimetr / 4)
        width = perimetr / 2
        return Rectangle(length, width)

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


rect1 = Rectangle(30, 5)
rect2 = Rectangle(26, 6)
print(rect1.width)
rect1.width = -100
print(rect1.width)