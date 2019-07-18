# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def createNum(node):
            val = 0
            while node:
                val = val*10 + node.val
                node = node.next
            return val
        
        val1, val2 = createNum(l1), createNum(l2)
        res = str(val1 + val2)
        
        head = node = ListNode(int(res[0]))
        for i in range(1, len(res)):
            temp = ListNode(int(res[i]))
            node.next = temp
            node = temp
        
        return head
        
        
        
