class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0:-1}
        max_len = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c -= 1
            else:
                c += 1

            if c in counts:
                max_len = max(max_len, i-counts[c])
            else:
                counts[c] = i

        return max_len
