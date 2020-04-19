class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == target:
                return mid
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi

            if nums[lo] < nums[hi]:
                if nums[mid] > target:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target > nums[hi]:
                    if nums[mid] < target:
                        lo +=1
                    else:
                        hi -=1
                else:
                    if nums[mid] < target:
                        lo +=1
                    else:
                        hi -= 1

        return -1
