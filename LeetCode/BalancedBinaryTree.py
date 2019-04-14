# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from math import inf

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balance(node, level):
            if not node:
                return True, level-1
            
            balanced1, height1 = balance(node.left, level + 1)
            balanced2, height2 = balance(node.right, level + 1)
            
            level = max(height1, height2)
            balanced = abs(height1 - height2) < 2
            
            if not balanced1 or not balanced2:
                return False, level

            return balanced, level 
        
        balanced, height = balance(root, 0)
        
        return balanced
            
