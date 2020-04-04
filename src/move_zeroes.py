class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 1:
            return nums
        z = 0
        n = 1
        while z != len(nums) and n != len(nums):
            if nums[n] == 0:
                n+=1
                continue
            if nums[z] == 0:
                nums[n],nums[z] = nums[z], nums[n]
                z+=1
                continue
            if z >= n: n+=1
            else: z+=1
        return nums
