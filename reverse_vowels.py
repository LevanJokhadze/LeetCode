class Solution:
    def __init__(self):
        self.vowels = set("aeiou")
        self.obj = {}
        self.arr = list()
        self.str = list()

    def reverseVowels(self, s: str) -> str:
        for i, char in enumerate(s):
            if char.lower() in self.vowels:
                self.arr.append(i)
                self.obj[i] = char

        self.str.extend(s)
        for xy in range(len(self.arr)):
            j = self.arr[xy]
            l = self.arr[len(self.arr) - 1 - xy]
            k = self.obj[l]
            self.str[j] = k

        return ''.join(self.str)


init = Solution()
result = init.reverseVowels("leetcode")
print(result)
