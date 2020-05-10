#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightMost = len(nums), 0
        for i in range(n):
            if i <= rightMost:
                rightMost = max(rightMost, i+nums[i])
                if rightMost >= n-1:
                    return True
        return False
# @lc code=end

