# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        
        
        def traverse(node):
            if not node:
                return 0, 0
            
            left_robbed, left_not_robbed = traverse(node.left)
            right_robbed, right_not_robbed = traverse(node.right)
            
            not_robbed = max(left_robbed + right_not_robbed, right_robbed + left_not_robbed, left_robbed + right_robbed, left_not_robbed + right_not_robbed )
            
            return left_not_robbed + right_not_robbed + node.val, not_robbed
        
        
        
        return max(traverse(root))
