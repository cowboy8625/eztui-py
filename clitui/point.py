class Point:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x + other.x), int(self.y + other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x + other), int(self.y + other))

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x - other.x), int(self.y - other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x - other), int(self.y - other))

    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x / other.x), int(self.y / other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x / other), int(self.y / other))

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(int(self.x * other.x), int(self.y * other.y))
        if isinstance(other, (int, float)):
            return Point(int(self.x * other), int(self.y * other))

    def __eq__(self, other):
        if isinstance(other, Point):
            return True if self.x == other.x and self.y == other.y else False

    def __hash__(self):
        return hash((self.x, self.y))


class Vector2(Point):

    """Container for Points of a 2D vector"""

    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        super().__init__(x, y)


class Vector3(Point):

    """Container for Points of a 3D vector"""

    __slots__ = ["x", "y", "z"]

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


def vct_to_idx(vct, width):
    if isinstance(vct, Vector2):
        x = vct.x
        y = vct.y
    else:
        x, y = vct
    return (width * x) + y
