#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {"A":"CGT","C":"AGT","G":"ACT","T":"ACG"}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, j in enumerate(node):
                    for c in change_map[j]:
                        new = node[:i] + c + node[i+1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(start_set) > len(end_set):
                start_set, end_set = end_set, start_set
        return -1

# @lc code=end

