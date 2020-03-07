# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def traverse(node, target):
            if not node:
                return None
            
            if node.val > target:
                return traverse(node.left, target)
            elif node.val < target:
                return traverse(node.right, target)
            else:
                return node
        
        return traverse(root, val)
