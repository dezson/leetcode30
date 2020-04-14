class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def help(s, amount, direction):
            if amount == 0:
                return s
            if direction == 0:
                return help(s[1:]+s[0], amount-1, direction)
            else:
                return help(s[-1]+s[:len(s)-1], amount-1, direction)

        for d,a in shift:
            s = help(s,a,d)
        return s
