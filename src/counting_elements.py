class Solution:
    def countElements(self, arr: List[int]) -> int:
        data = {}
        cnt = 0
        for e in sorted(arr):
            if e-1 in data:
                cnt+=data[e-1]
                data[e-1] = 0

            if e in data:
                data[e] += 1
            else:
                data[e] = 1
        return cnt
