class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(l):
            ans = []
            for ch in l:
                if ch != "#":
                    ans.append(ch)
                elif ans:
                    ans.pop()

            return ans
