# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head, prev = head, None
        counter = 1
        while counter != m:
            prev = head
            head = head.next
            counter+=1

        temp2 = head.next
        end_of_reverse = head
        
        while m != n:
            temp = temp2
            temp2 = temp.next
            temp.next = head
            head = temp
            m+=1
            
        tail = temp2

        if prev:
            prev.next = head
        else:
            dummy_head = head
        end_of_reverse.next = tail
        
        return dummy_head
        
