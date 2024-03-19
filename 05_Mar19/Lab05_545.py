import copy

class Vector:
    def __init__(self, n):
        if isinstance(n, Vector):
            # дані self <- дані з n
            self._data = copy.deepcopy(n._data)
        elif isinstance(n, list):
            self._data = copy.deepcopy(n)
        else:
            self._data = [0.0]*n
    def __len__(self):
        return len(self._data)
    def __getitem__(self, j):
        return self._data[j]
    def __setitem__(self, j, val):
        # тут можуть бути додаткові перевірки
        self._data[j] = val
    def __str__(self):
        s = 'Vec: '
        s += ', '.join(map(str, self._data))
        return s
    def __add__(self, other):
        res = Vector(self)
        if isinstance(other, Vector):
            # покомпонентна сума двох векторів
            for i in range(len(res)):
                res[i] += other[i]
            return res
        else:
            # додавання числа до всіх компонент
            for i in range(len(res)):
                res[i] += other
            return res
    def __radd__(self, other):
        return self.__add__(other)
        #return self + other # також можна


a = Vector( [
    Vector([1, 2]),
    Vector([-2, -1])
    ]
)

a = a + 10
print(a)

