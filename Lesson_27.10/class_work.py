# class X:
#     def __init__(self):
#         self.x = 0
#
#     def func(self):
#         print(self.x)
#
#
# a = X()
# b = X()
#
# a.x = 3
# b.x = 1
# a.func()
# b.func()

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # def get_phi(self):

    def __str__(self):
        return f"Vector2D with: x = {self.x}, y = {self.y}"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector2D(self.x + other, self.y)

    def __radd__(self, other):
        return Vector2D(self.x + other, self.y)







a = Vector2D(4, 3)
b = Vector2D()
print(a, type(a))
print(type(4))
print(a.x, a.y)
print(b.x, b.y)
print(abs(a), abs(b))
a.x = 6
a.y = 8
print(abs(a))
b.x = 2
b.y = 3
c = a + b  # a.__add__(b)
print(c.x, c.y)
print(c)
print(a + 10)
print(10 + a)
# class Point:
#     def __init__(self, m, x=0, y=0, vx=0, vy=0):
#         self.m = m
#         self.x = x
#         self.y = y
#         self.vx = vx
#         self.vy = vy
#         self._ax = 0
#         self._ay = 0
#
#     def net_force(self, Fx, Fy):
#         self._ax += Fx / self.m
#         self._ay += Fy / self.m
#
#     def move(self, dt):
#         self.vx += self._ax * dt
#         self.vy += self._ay * dt
#
#         self.x += self.vx * dt
#         self.y += self.vy * dt
#
#         self._ax = 0
#         self._ay = 0
#
#
# g = 10
# points = [Point((i + 1) ** 2, i, i) for i in range(10)]
#
# dt = 10 ** -2
# t = 5
# for i in range(int(t / dt)):
#     for point in points:
#         point.net_force(0, -point.m * g)
#         point.net_force(0.05, 0)
#         point.move(dt)
#
# for point in points:
#     print(point.x, point.y)
#
# print(points[0]._ax)