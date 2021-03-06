#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return nums
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
        
