# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        def traverse(node1, node2):
            
            if node1 and node2:
                node1.val+=node2.val
            
            if not node2:
                return
                
            
            if not node1.left and node2.left:
                node1.left = node2.left
            else:
                traverse(node1.left, node2.left)
            
            
            if not node1.right and node2.right:
                node1.right = node2.right
            else:
                traverse(node1.right, node2.right)
                
        
        traverse(t1, t2)
        return t1
            
            
