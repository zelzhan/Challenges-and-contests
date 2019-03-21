# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        if left.val!= right.val:
            return False
        if not self.isMirror(left.left, right.right):
            return False
        if not self.isMirror(left.right, right.left):
            return False
        return True
        
        
        
            
        
        
        
