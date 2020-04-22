class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}
        ans = 0
        curr_sum = 0
        for i in range(0 ,len(nums)):
            curr_sum+=nums[i]
            if curr_sum == k:
                ans+=1
            if curr_sum - k in memo:
                ans += memo[curr_sum - k]

            if curr_sum not in memo:
                memo[curr_sum] = 1
            else:
                memo[curr_sum]+=1

        return ans
