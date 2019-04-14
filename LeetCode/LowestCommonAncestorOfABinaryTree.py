# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lca(node, value1, value2):
            if not node:
                return 
            if node.val == value1.val or node.val == value2.val:
                return node
            val1, val2 = lca(node.left, value1, value2), lca(node.right, value1, value2)
            if val1 and val2:
                return node
            elif val1:
                return val1
            elif val2:
                return val2
            
        return lca(root, p, q)
        
        
