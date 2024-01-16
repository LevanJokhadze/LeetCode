class Solution:
    def __init__(self):
        self.arr = list()
    def search(self, arr: list[int], targ: int) -> list[int]:
        leng = len(arr)
        for keys in range(leng):
            for i in range(leng):
                temp = arr[keys] + arr[i]
                if temp == targ:
                    self.arr.append(keys)
                    self.arr.append(i)
                    return self.arr


init = Solution()
print(init.search([2, 7, 11, 5], 9))
