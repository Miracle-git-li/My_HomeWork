#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        i = 0
        j = len(s) - 1
        while i <= j:
            if i < j and not s[i].isalpha():
                i += 1
            elif i < j and not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
        
# @lc code=end

