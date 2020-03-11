"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import sys
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        max_depth = [0]
        def traverse(node, depth=1):
            if node:
                if depth > max_depth[0]:
                    max_depth[0] = depth

                for child in node.children:
                    traverse(child, depth=depth+1)
        
        traverse(root)
        return max_depth[0]
        
