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
        se = set(s)
        if se == set(t):
            for i in se:
                if s.count(i) != t.count(i):
                    return False
                
            return True
        else:
            return False



# @lc code=end

