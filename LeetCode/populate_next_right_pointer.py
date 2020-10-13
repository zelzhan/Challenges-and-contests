"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque()
        prev = Node()
        queue.append((0, prev))
        queue.append((0, root))
        
        prev_level = -1
        
        while queue:
            level, node = queue.popleft()
            
            
            if level > prev_level:
                prev_level = level
                prev = node
            else:
                prev.next = node
                prev = node
                
            
            if node.left:
                queue.append((level+1, node.left))
            
            if node.right:
                queue.append((level+1, node.right))
        
        return root
            
            
        
