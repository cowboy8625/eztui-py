
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def from_index(cls, width, height, index):
        x = index % width
        y = int(index / width)
        return cls(x, y)

    def __str__(self):
        if hasattr(self, "_index"):
            return f"Point({self.x}, {self.y}, {self.index})"
        else:
            return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        return True if ((self.x == other.x) and (self.y == other.y)) else False

    def __nq__(self, other):
        return True if ((self.x != other.x) and (self.y != other.y)) else False

    def __sub__(self, other):
        return Point((self.x - other.x), (self.y - other.y))

    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        return Point((self.x * other.x), (self.y * other.y))
        
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def index(self):
        return self._index


