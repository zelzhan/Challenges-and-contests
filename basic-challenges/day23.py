import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    #Solution
    def levelOrder(self,root):
        from collections import deque
        q = deque([root]) if root else deque([])
#        if(root): q = deque([root]) else: deque([])
        while True:
            element = q.popleft()
            print(element.data, end=" ")
            if(element.left): q.append(element.left)
            if(element.right): q.append(element.right)
            if(len(q)==0): break

#Test
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

