#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        for i in range(0, len(s), 2*k):
            tmp = s[i:i+k]
            tmp = tmp[::-1] + s[i+k:i+2*k]
            res += tmp
        return res
        
# @lc code=end

