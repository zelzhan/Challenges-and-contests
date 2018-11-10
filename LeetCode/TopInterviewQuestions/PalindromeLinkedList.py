'''Given a singly linked list, determine if it is a palindrome.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        odd = False
        
        if not head: 
            return True
        elif not head.next:
            return True

        while fast:
            if fast.next == None:
                odd = True
                break
            prev = slow
            slow = slow.next
            fast = fast.next.next

        temp = None
        prev.next = None
        
        if odd:
            slow = slow.next
            
        while slow:
            temp2 = slow.next
            slow.next = temp
            temp = slow
            slow = temp2
        temphead = head
        
        while temp:
            if temp.val != head.val:
                return False

            temp = temp.next
            head = head.next

        return True
        
        
        
        
        
        
        
