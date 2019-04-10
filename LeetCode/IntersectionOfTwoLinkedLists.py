# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        head1, head2 = headA, headB
        length1, length2 = 0, 0
        while headA and headB:
            headA = headA.next
            headB = headB.next
            length1+=1
            length2+=1
        
        if headA:
            while headA:
                length1+=1
                headA = headA.next
        else:
            while headB:
                length2+=1
                headB = headB.next
        
        if length1 > length2:
            while length1 != length2:
                length1-=1
                head1 = head1.next
        else:
            while length1 != length2:
                length2-=1
                head2 = head2.next
        
        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        
        return None
            
        
            
        
