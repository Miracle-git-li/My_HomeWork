#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dicts = {5:0, 10:0}
        for i in bills:
            if i == 5:
                dicts[5] += 1
            elif i == 10:
                if dicts[5] < 1:
                    return False
                dicts[5] -= 1
                dicts[10] += 1
            elif i == 20:
                if dicts[10] < 1 and dicts[5] < 3:
                    return False
                if dicts[5] < 1:
                    return False
                if dicts[10] >= 1:
                    dicts[10] -= 1 
                    dicts[5] -= 1
                else: dicts[5] -= 3
        return True
# @lc code=end

