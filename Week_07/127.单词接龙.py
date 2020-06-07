#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        begin_set = {beginWord}
        end_set = {endWord}
        wordList = set(wordList)
        res = 1
        length = len(beginWord)
        while begin_set:
            res += 1
            new_set = set()
            for word in begin_set:
                for i in range(length):
                    for c in string.ascii_lowercase:
                        new = word[:i] + c + word[i+1:]
                        if new in end_set:
                            return res
                        if new in wordList:
                            new_set.add(new)
                            wordList.remove(new)
            begin_set = new_set
            if len(end_set) < len(begin_set):
                end_set, begin_set = begin_set, end_set
        return 0
# @lc code=end

