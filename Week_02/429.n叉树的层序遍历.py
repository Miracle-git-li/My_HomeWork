#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        k = len(res)
        def ntree(root, k):
            if root is None:
                return
            if k == len(res):
                res.append([])
            res[k].append(root.val)
            for i in root.children:
                ntree(i, k+1)
        ntree(root, k)
        return res

     
            
           
# @lc code=end

