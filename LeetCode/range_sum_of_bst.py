# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        def traverse(node, l, r, res=0):
            if not node:
                return 0
            
            if l <= node.val <= r:
                res+=node.val
                res+=traverse(node.left, l, r)
                res+=traverse(node.right, l, r)
            elif r < node.val:
                res+=traverse(node.left, l, r, res)
            else:
                res+=traverse(node.right, l, r, res)
            return res
        
    
        return traverse(root, L, R)
            
            
