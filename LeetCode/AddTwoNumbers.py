'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 2 > 4 > 3
    # 5 > 6 > 4 quot rem
    # 7 > 0 > 8 
    def traverse(self, node, root, quot):
        while node:
            root.next = ListNode((node.val + quot) % 10 )
            root = root.next
            quot = (node.val + quot) // 10
            node = node.next
        if quot:
            root.next = ListNode(quot)
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Case 1:
        # 2 > 4 > 3
        # 5 > 6 > 4
        # 7 > 0 > 7 
        
        #Case 2:
        # 2 > 4 > 9 > 9
        # 3 > 2 > 1
        # 5 > 6 > 0 > 2
        
        root = head = ListNode(0)
        quot = 0
        while l1 and l2:
            root.val = (l1.val + l2.val + quot) % 10
            quot = (l1.val + l2.val + quot) // 10
            l1 = l1.next
            l2 = l2.next
            if not l1 or not l2:
                break
            root.next = ListNode(0)
            root = root.next
        
        if l1:
            self.traverse(l1, root, quot)
        elif l2:
            self.traverse(l2, root, quot)
        elif quot:
            root.next = ListNode(quot)
            
        return head
