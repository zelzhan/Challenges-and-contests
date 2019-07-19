"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        def create_duplicates(node):
            while node:
                hashtable[node] = Node(node.val, None, None)
                node = node.next
        
        def map_nodes(node):
            while node:
                if node.next:
                    hashtable[node].next = hashtable[node.next]
                if node.random:
                    hashtable[node].random = hashtable[node.random]
                node = node.next
        
        hashtable = dict()
        create_duplicates(head)
        map_nodes(head)
        
        return hashtable[head]
    
    
    
        
        
            
