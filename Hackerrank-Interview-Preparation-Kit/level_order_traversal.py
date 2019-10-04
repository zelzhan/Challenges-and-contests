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
        # 3
        # 9 20
        # 15 7
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        counter = 1
        while queue:
            next_counter = 0
            level = []
            while counter:
                node = queue.popleft()
                if node.left:
                    next_counter+=1
                    queue.append(node.left)
                if node.right:
                    next_counter+=1
                    queue.append(node.right)
                level.append(node.val)
                counter-=1
            counter = next_counter
            res.append(level)
            
        return res
        
        
