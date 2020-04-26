#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def recur(root):
            if root is None:
                return None
            res.append(root.val)
            children = root.children
            for child in children:
                recur(child)
        recur(root)
        return res
               
        


        
# @lc code=end

