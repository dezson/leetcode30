class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = " " + text1
        s2 = " " + text2
        dp = [[0 for z in range(0,len(s2))] for _ in range(0,len(s1))]

        for i in range(1, len(s1)):
            for k in range(1, len(s2)):
                if s1[i] == s2[k]:
                    dp[i][k] = dp[i-1][k-1] + 1
                else:
                    dp[i][k] = max(dp[i-1][k], dp[i][k-1])
        return dp[-1][-1]
