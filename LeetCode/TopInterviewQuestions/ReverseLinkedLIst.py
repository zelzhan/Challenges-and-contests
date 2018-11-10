'''reverse linked list'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #  None <- 1  2 -> 3 -> 4 -> 5 -> None
        
        prev = None
        
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        
        return prev
        
        
