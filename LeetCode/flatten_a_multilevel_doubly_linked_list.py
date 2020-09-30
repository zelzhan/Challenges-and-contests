"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

from collections import deque
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        stack = [head]
        
        prev = Node(0, None, None, None)
        
        while stack:
            node = stack.pop()
            
            prev.next = node
            node.prev = prev
            
            if node.next:
                stack.append(node.next)
            
            if node.child:
                stack.append(node.child)
                node.child = None
                
            prev = node
            
        
        head.prev = None

        return head
            
            
            
