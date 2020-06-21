#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic_ = {}
        for i in s:
            dic_[i] = dic_.get(i, 0) + 1
        for i in dic_:
            if dic_[i] == 1:
                return s.index(i)
        return -1
# @lc code=end

