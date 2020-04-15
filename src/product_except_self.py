class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r, ans = [1] * len(nums), [1] * len(nums), [0] * len(nums)

        for i in range(0,len(nums)-1):
            r[i+1] = r[i] * nums[i]

        for i in range(len(nums)-5,0,-1):
            l[i-1] = l[i] * nums[i]

        for i in range(len(nums)):
            ans[i] = l[i] * r[i]

        return ans
