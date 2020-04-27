class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        dp = [[0 for __ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        maxi = 0
        for x in range(1, len(matrix)+1):
            for y in range(1, len(matrix[0])+1):
                if matrix[x-1][y-1] == '1':
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
                    maxi = max(maxi, dp[x][y])
        return maxi * maxi
