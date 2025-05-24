class List:
    def __init__(self):
        self._values = []

    def add_value(self, value):
        self._values.append(value)
        return print('Значение добавлено')

    def remove_value(self, value):
        if value in self._values:
            self._values.remove(value)
        return print('Значение удалено')
    def get_elem(self, values, ind):
        print(values[ind])
    def get_Elem(self, ind):
        if 0 <= ind < len(self._values):
            return self._values[ind]
        else:
            print('Error')
    def set_Elem(self,ind,val):
        if 0 <= ind < len(self._values):
            self._values[ind] = val
        else:
            print('OSHIBKA')
    def get_avg(self):
        avg = sum(self._values) / len(self._values)
        return avg
    def get_SD(self):
        avg= (self.get_avg())
        D = sum([(x - avg) ** 2 for x in self._values]) / len(self._values)
        return print('Среднеквадратическое отклонение:',D)

vl = List()
vl.add_value(10)
vl.add_value(20)
vl.add_value(30)
vl.add_value(40)
vl.remove_value(40)

print(vl._values)
print(vl.get_Elem( 2))
print(vl.set_Elem( 1,  2))
print(vl._values)
print(vl.set_Elem( 1,  20))
print(vl._values)
print(print('Среднеарифметическое значение:'), vl.get_avg())
print(vl.get_SD())