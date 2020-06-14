#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        def DFS(queue, xy_diff, xy_sum):
            p = len(queue)
            if p == n:
                res.append(queue)
            for q in range(n):
                if q not in queue and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queue+[q], xy_diff+[p-q], xy_sum+[p+q])
        DFS([],[],[])
        return len(res)
# @lc code=end

