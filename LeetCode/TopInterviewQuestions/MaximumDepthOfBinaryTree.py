'''Given a binary tree, find its maximum depth.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def traverse(self, root):
        
        if not root.left and not root.right:
            return 1
        val1, val2 = 0, 0
        
        if root.left:
            val1 = self.traverse(root.left)
        
        if root.right:
            val2 = self.traverse(root.right)
    
        return 1 + max(val1, val2)
    
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.traverse(root)
        
