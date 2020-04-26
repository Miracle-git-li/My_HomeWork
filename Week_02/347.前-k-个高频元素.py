#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_max = []
        dic_fre = {}
        res = []
        for i in nums:
            if i in dic_fre:
                dic_fre[i] += 1
            else:
                dic_fre[i] = 1
        for i in dic_fre:
            heapq.heappush(heap_max, (-dic_fre[i],i))
        for j in range(k):
            p = heapq.heappop(heap_max)
            res.append(p[1])
        return res
# @lc code=end

