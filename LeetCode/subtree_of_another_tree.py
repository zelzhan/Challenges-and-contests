# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right):
                return True
            return False
        
        def traversal(s, t):
            if not s:
                return False
            if s.val == t.val and sameTree(s, t):
                return True
            else:
                return traversal(s.left, t) or traversal(s.right, t)
                
        return traversal(s, t)
                
                    
                    
