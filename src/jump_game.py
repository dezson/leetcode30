class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        for i in range(1,len(nums)-1):
            nums[i] = max(nums[i],nums[i-1]-1)
            if nums[i] == 0:
                return False

        return True if nums[len(nums)-2] > 0 else False
