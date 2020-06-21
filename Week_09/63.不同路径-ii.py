#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m < 1 or n < 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif j == 0 and i != 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i-1][j]
                elif i == 0 and j != 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j-1]
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# @lc code=end

