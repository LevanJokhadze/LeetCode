class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        zeros = 0
        print(flowerbed)
        for key, value in enumerate(flowerbed):
            if value == 1:
                if key + 1 < len(flowerbed):
                    flowerbed[key + 1] = 2
                    if flowerbed[-1] == 1:
                        flowerbed[len(flowerbed) - 2] = 2
                if key - 1 != -1:
                    flowerbed[key - 1] = 2
            if key + 1 < len(flowerbed):
                if value == 0 and flowerbed[key + 1] != 1:
                    if key != (len(flowerbed) - 1):
                        flowerbed[key + 1] = 2
                        if key - 1 != -1:
                            flowerbed[key - 1] = 2
        print(flowerbed)
        for i in flowerbed:
            if i == 0:
                zeros += 1
        return zeros >= n


init = Solution()
print(init.canPlaceFlowers([0, 1], 1))
