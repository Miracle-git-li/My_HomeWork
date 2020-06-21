#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        res = ""
        s = s + " "
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res += stack.pop()
        return res[1:]
    
        
# @lc code=end

