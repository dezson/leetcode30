class Solution:
    def isHappy(self, n: int) -> bool:
        past = {}
        while n != 1:
            if n in past:
                return False
            else:
                past[n] = None
            sum = 0
            while n != 0:
                sum += (n % 10) ** 2
                n //= 10
            n = sum 
        return True

