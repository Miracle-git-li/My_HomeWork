#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_set = set(t)
        for i in set(s):
            if i not in t_set:
                return False
            if t.count(i) != s.count(i):
                return False
        return True
# @lc code=end

