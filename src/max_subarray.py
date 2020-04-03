class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        max_so_far = nums[0]
        xam = nums[0]
        for i in range(1,len(nums)):
            xam += nums[i]
            if nums[i] > xam:
                xam = nums[i]
            if xam > max_so_far:
                max_so_far = xam
        return max_so_far
