# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #               1
        #              /  \
        #             2    3
        #            / \ 
        #           4   5
        
        
        if not root:
            return 0
        res = [0]
        def helper(node, result, is_left):
            if not node:
                return
            
            if not node.left and not node.right and is_left:
                result[0]+=node.val
            
            helper(node.left, result, True)
            helper(node.right, result, False)
        
        
            
        helper(root, res, False)
        return res[0]
            
            
            
        
