# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        
        if not head:
            return None
        elif k == 0:
            return head
        
        def length(head):
            counter = 0
            while head:
                head = head.next
                counter+=1
            return counter
            
        k = k%length(head)
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_head = head
        def return_m_from_the_end(node, m):
            if not node:
                return None
            first, second = node, node
            for _ in range(m+1):
                second = second.next
            while second:
                first = first.next
                second = second.next    
            return first
        
        temp = return_m_from_the_end(head, k)
        if not temp.next:
            return dummy_head

        node = res = temp.next
        temp.next = None       
        
        while node.next:
            node = node.next
        
        node.next = dummy_head
        
        return res
        
        
        
        
        
        
        
        
        
        
        
