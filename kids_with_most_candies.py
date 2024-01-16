class Solution:
    def __init__(self):
        self.arr = list()
        self.ret = list()

    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        gr = max(candies)
        for i in candies:
            i += extraCandies
            self.arr.append(i)
        for x in self.arr:
            if x >= gr:
                self.ret.append(True)
            else:
                self.ret.append(False)
        return self.ret


init = Solution()
print(init.kidsWithCandies([12,1,12], 10))
