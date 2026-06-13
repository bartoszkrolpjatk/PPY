import math

class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vec2D): return NotImplemented
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__ (self, other):
        if not isinstance(other, Vec2D): return NotImplemented
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec2D(other * self.x, other * self.y)
        elif isinstance(other, Vec2D):
            return Vec2D(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if not isinstance(other, Vec2D): return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"V[{self.x}, {self.y}]"

    @property
    def magnitude(self):
        return math.hypot(self.x, self.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = float(new_x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = float(new_y)

va, vb = Vec2D(3, 4), Vec2D(-1, 2)
vc = 2*va - vb*3 + Vec2D(0, 10)
vd = vc * va
print(va, vb, vc, vc.magnitude, vd)
print(vd == Vec2D(27, 48))