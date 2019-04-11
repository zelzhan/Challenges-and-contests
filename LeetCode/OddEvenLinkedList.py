# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1 -> 2 -> 3
        if not head:
            return None
        pointer1, pointer2 = head, head.next
        odd = pointer1
        even = pointer2
        while pointer1.next and pointer1.next.next:
            pointer1.next = pointer2.next
            pointer1 = pointer2.next
            
            pointer2.next = pointer1.next
            pointer2 = pointer1.next
        
        pointer1.next = even
        return head
