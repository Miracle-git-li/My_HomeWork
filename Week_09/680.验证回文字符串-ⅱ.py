#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda s: s == s[::-1]
        strPalindrome = lambda s, x: s[:x] + s[x+1:]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPalindrome(s, left)) or isPalindrome(strPalindrome(s, right))
            else:
                left += 1
                right -= 1
        return True     
        
# @lc code=end

