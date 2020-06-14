#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def DFS(queue, xy_diff, xy_sum):
            p = len(queue)
            if p == n:
                res.append(queue)
            for q in range(n):
                if q not in queue and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queue+[q], xy_diff+[p-q], xy_sum+[p+q])
        DFS([],[],[])
        return [['.'*i+"Q"+"."*(n-i-1) for i in row]for row in res]
# @lc code=end

