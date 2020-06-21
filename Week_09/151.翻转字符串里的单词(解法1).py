#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        if not s: return ""
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i+1:j+1])
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i
        return " ".join(res)

            
# @lc code=end

