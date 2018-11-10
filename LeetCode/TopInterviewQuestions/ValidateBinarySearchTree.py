'''Given a binary tree, determine if it is a valid binary search tree (BST).'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findmax(self, root):
        
        if not root.right and not root.left:
            return root.val
        
        max1, max2 = root.val, root.val
        if root.left:
            max1 = self.findmax(root.left)
        if root.right:
            max2 = self.findmax(root.right)
        
        return max(max1, max2, root.val)
    
    
    def findmin(self, root):
        
        if not root.right and not root.left:
            return root.val
        
        min1, min2 = root.val, root.val
        if root.left:
            min1 = self.findmin(root.left)
        if root.right:
            min2 = self.findmin(root.right)
        
        return min(min1, min2, root.val)
        
    def helper(self, root):
        if not root:
            return True
        
        if not root.left and not root.right:
            return True

        validleft, validright = True, True
        
        if root.right:
            validright = root.right.val > root.val and self.findmin(root.right) > root.val
        
        if root.left:
            validleft = root.left.val < root.val and self.findmax(root.left) < root.val
            
        if not validleft or not validright:
            return False
        
        return self.helper(root.left) and self.helper(root.right)
    
    def isValidBST(self, root):
        
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root)
        
        
