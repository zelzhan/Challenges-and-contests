# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def solve(node):
            if node:
                begin1, end1 = solve(node.left)
                begin2, end2 = solve(node.right)
                
                if begin1:
                    node.right = begin1
                    end1.right = begin2
                else:
                    node.right = begin2
                
                node.left = None
                
                if end2:
                    return node, end2
                elif end1:
                    return node, end1

                return node, node
            return None, None
            
        
        solve(root)
