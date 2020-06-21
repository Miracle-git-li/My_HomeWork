#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s: return True
        dic = {}
        for i in range(len(s)):
            if not s[i] in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True
        
# @lc code=end

