class Rectangle:
    def __init__(self, h, a):
        self.__a = a
        self.__h = h
        self.__s = self.calculate_s()
        self.__p = self.calculate_p()

  
    def calculate_s(self):
        return self.__a * self.__h


    def calculate_p(self):
        return 2 * (self.__a + self.__h)

    def get_h(self):
        return self.__h

    def set_h(self, h):
        self.__h = h
        self.__s = self.calculate_s()
        self.__p = self.calculate_p()

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a
        self.__s = self.calculate_s()
        self.__p = self.calculate_p()

    def get_s(self):
        return self.__s

    def get_p(self):
        return self.__p

r = Rectangle(5, 3)
print("Высота:", r.get_h())
print("Длина:", r.get_a())
print("Площадь:", r.get_s())
print("Периметр:", r.get_p())
