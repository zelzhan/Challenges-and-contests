'''Given a linked list, remove the n-th node from the end of list and return its head.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1 - 2 - 3 - 4 - 5
        # slow = 1
        # fast = 5
        # k = 5
        
        slow = fast = head
        
        for i in range(n):
            fast = fast.next
            
        if fast == None:
            slow = None
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return head
        
