class Sorter:
    def __init__(self):
        self.a = list()
        self.b = list()

    def sorter(self, arr: list[int]):
        self.a = arr
        self.b = sorted(self.a)
        x, y = 0, 1
        m = len(self.a) - 1
        while self.a != self.b:
            if self.a[x] > self.a[y]:
                self.a[x], self.a[y] = self.a[y], self.a[x]
            x += 1
            y += 1
            if y == m + 1:
                x, y = 0, 1
        return self.a


init = Sorter()
print(init.sorter([5, 3, 7, 4, 1, 11, 9]))

