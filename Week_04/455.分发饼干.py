#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child = 0
        size = 0
        g.sort()
        s.sort()
        while child < len(g) and size < len(s):
            if g[child] <= s[size]:
                child += 1
                size += 1
            else: size += 1
        return child 
        
# @lc code=end

