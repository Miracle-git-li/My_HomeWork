#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) <= 2:
            return res
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            l = len(nums) - 1 
            while j < l:
                sum = nums[i] + nums[j] + nums[l]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    l -= 1
                else:
                    res.append([nums[i], nums[j], nums[l]])
                    while j < l and nums[j] == nums[j+1]:
                        j += 1
                    while j < l and nums[l] == nums[l-1]:
                        l -= 1
                    l -= 1
                    j += 1
        return res



# @lc code=end

