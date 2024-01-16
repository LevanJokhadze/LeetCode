class Solution:
    def __init__(self):
        self.arr_1 = list()
        self.arr_2 = list()
        self.arr = list()

    def mergeAlternately(self, param_1: str, param_2: str) -> str:
        w1 = len(param_1)
        w2 = len(param_2)

        if w1 < w2:
            w = w1
        else:
            w = w2
        ids = 0

        for i in range(w):
            self.arr.append(param_1[ids])
            self.arr.append(param_2[ids])
            ids += 1

        if w1 < w2:
            w = w2
            for x in param_2:
                if ids == w2:
                    break
                self.arr.append(param_2[ids])
                ids += 1
        else:
            w = w1
            for x in param_1:
                if ids == w1:
                    break
                self.arr.append(param_1[ids])
                ids += 1
        mystr = ''
        for x in self.arr:
            mystr += "" + x
        return mystr


init = Solution()
print(init.mergeAlternately("abcd", "pq"))




