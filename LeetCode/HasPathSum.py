# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def path_sum(node, value, target):
            if not node:
                return False
            value += node.val
            if value == target and not node.left and not node.right:
                return True
            return path_sum(node.left, value, target) or path_sum(node.right, value, target)
        
        return path_sum(root, 0, sum)
