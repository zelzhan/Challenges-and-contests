# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = head
        while head and head.next:
            temp = head
            while temp.next and temp.val == temp.next.val:
                temp = temp.next
            head.next = temp.next
            head = head.next
        return dummy_head
        
