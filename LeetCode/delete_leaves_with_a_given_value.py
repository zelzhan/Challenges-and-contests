# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def is_leaf(node):
            if not node.left and not node.right:
                return True
            return False
        
        
        def helper(node, target, parent = None):
            if node:
                helper(node.left, target, node)
                helper(node.right, target, node)

                if node.val == target and is_leaf(node) and parent:
                    if parent.left is node:
                        parent.left = None
                    if parent.right is node:
                        parent.right = None

        helper(root, target)
        if root.val == target and is_leaf(root):
            return None
        
        return root
        
