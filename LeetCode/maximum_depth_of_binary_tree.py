# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def traverse(node, depth=0):
            if not node:
                return depth
            
            return max(traverse(node.left, depth+1), traverse(node.right, depth+1))
            
            
        return traverse(root)
            
        
