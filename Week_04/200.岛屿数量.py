#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        IlandNum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    IlandNum += 1
                    self.clear_zero(grid, i, j)
        return IlandNum
    def clear_zero(self, arr, x, y):
        arr[x][y] = "0"
        if x-1 >= 0 and arr[x-1][y] =="1":
            self.clear_zero(arr, x-1, y)
        if x+1 < len(arr) and arr[x+1][y] == "1":
            self.clear_zero(arr, x+1, y)
        if y-1 >= 0 and arr[x][y-1] == "1":
            self.clear_zero(arr, x, y-1)
        if y+1 < len(arr[0]) and arr[x][y+1] == "1":
            self.clear_zero(arr, x, y+1)
        return None
# @lc code=end

