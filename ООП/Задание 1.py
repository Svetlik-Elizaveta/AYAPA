def Int(n):
    a = input( {n} )
    x, y = map(float, a.split())
    return Dot(x, y)


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_dot(self):
        print('(',self.x , self.y, ')')


class Vector:
    def __init__(self, dot1: Dot, dot2: Dot):
        self.dot1 = dot1
        self.dot2 = dot2

    @property
    def x(self):
        return self.dot2.x - self.dot1.x

    @property
    def y(self):
        return self.dot2.y - self.dot1.y

    def add(self, other):
        coord1 = Dot(0, 0)
        coord2 = Dot(self.x + other.x, self.y + other.y)
        return Vector(coord2, coord1)

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def print_vector(self):
        print(f"Длина вектора: {self.length}")


dot1 = Int(1)
dot2 = Int(2)
dot3 = Int(3)
print(dot1.print_dot(),dot2.print_dot(),dot3.print_dot())
c = Vector(dot1, dot2)
c.print_vector()