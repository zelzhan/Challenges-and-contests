class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    #My solution (little bit complicated)
    def removeDuplicates(self,head):
        node = head
        while node is not None and node.next is not None:       
            if node.data == node.next.data:
                nextnode = node
                while nextnode.data == nextnode.next.data:
                    nextnode = nextnode.next
                    if nextnode.next is None: break
                node.next = nextnode.next
            node = node.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
