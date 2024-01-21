class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        i, j = 0, len(nums) - 1
        z = 0
        while i < j:
            if nums[i] == 0:
                nums.pop(i)
                j -= 1
                z += 1
            else:
                i += 1
        for i in range(z):
            nums.append(0)
        return nums


init = Solution()
x = init.moveZeroes([0,0,1,12,0,2,0,0])
