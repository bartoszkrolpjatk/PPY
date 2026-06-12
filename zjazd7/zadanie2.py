import functools

@functools.total_ordering
class Interval:

    def __init__(self, a, b):
        self._a = min(a, b)
        self._b = max(a, b)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    def __repr__(self):
        return f"[{self.a}, {self.b}]"

    def __len__(self):
        return self.b - self.a

    def __and__(self, other):
        if not self.intersects(other): raise ValueError("Intervals do not intersect!")
        return Interval(max(self.a, other.a), min(self.b, other.b))

    def __or__(self, other):
        return Interval(min(self.a, other.a), max(self.b, other.b))

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return (self.a, self.b) < (other.a, other.b)

    def intersects(self, other):
        return self.a <= other.b and self.b >= other.a


inter1 = Interval(1, 5)
inter2 = Interval(1, 2)
print(inter1 > inter2)


i1, i2, i3 = Interval(2, 7), Interval(-4, 4), Interval(-8, 1)

print('Intervals:', i1, i2, i3)
print('Lengths: ', len(i1), len(i2), len(i3))
print('i1 & i2, i1 & i3, i2 & i2 exist?', i1.intersects(i2), i1.intersects(i3), i2.intersects(i3))
print('i1&i2 =', i1 & i2, ' i2&i3 =', i2 & i3)
print('i1|i2 =', i1 | i2, ' i1|i3 =', i1 | i3, ' i2|i3 =', i2 | i3)
lst = [i1, i2, i3]
print('Unsorted:', lst)
lst.sort()
print('Sorted: ', lst)