'''Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Overwrite all values in linked list
class Solution:
    def deleteNode(self, node):
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if not node.next.next:
            node.val = node.next.val
            node.next = None
            return
        
        
        runnerup = node
        
        while runnerup.next:
            node.val = node.next.val
            node = node.next
            runnerup = node.next
        
        node.val = runnerup.val
        node.next = None
        
