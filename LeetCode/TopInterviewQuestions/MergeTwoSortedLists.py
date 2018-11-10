'''Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 3 5 6
        # 2 4 8
        # 1 -> None
        
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
                
        if l1.val < l2.val:
            temp = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = ListNode(l2.val)
            l2 = l2.next
   
        head = temp
    
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
            
        if not l1:
            while l2:
                temp.next = ListNode(l2.val)
                l2 = l2.next
                temp = temp.next
        if not l2:
            while l1:
                temp.next = ListNode(l1.val)
                l1 = l1.next
                temp = temp.next
        return head
        
