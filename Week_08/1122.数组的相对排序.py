#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num = [0] * 1001
        res= []
        for i in arr1:
            num[i] += 1
        for j in arr2:
            if num[j] > 0:
                res += [j]*num[j]
                num[j] = 0
        for n in range(len(num)):
            if num[n] > 0:
                res += [n]*num[n]
        return res
# @lc code=end

