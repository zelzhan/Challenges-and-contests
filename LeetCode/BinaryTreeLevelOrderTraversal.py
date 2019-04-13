# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque()
        level = [root]
        res = []
        while level:
            res.append([node.val for node in level])
            level = [
                node
                for element in level 
                for node in (element.left, element.right)
                if node
            ]
        
        return res
