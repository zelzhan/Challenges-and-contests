# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [] 
        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                res.append(node.val)
        helper(root)
        return res
        
