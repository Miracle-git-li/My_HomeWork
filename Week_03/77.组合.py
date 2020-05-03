#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(i, k , tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                back(j+1, k-1, tmp+[j])
        back(1, k, [])
        return res

# @lc code=end

