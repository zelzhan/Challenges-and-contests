"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []
        def traverse(node):
            if not node:
                return
            
            for el in node.children:
                traverse(el)
            
            res.append(node.val)
        
        traverse(root)
        return res
