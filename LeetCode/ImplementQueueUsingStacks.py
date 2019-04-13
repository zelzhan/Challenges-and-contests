class MyQueue(object):
    # 1 2 3 4 5 6
    # pop() or peek()
    # stack1 4 5
    # stack2 3 2 1

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        
        
    
    def __shuffle(self):
        self.stack1.reverse()
        self.stack2 = self.stack1
        self.stack1 = []
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            self.__shuffle()
        
        return self.stack2.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2:
            self.__shuffle()
        
        return self.stack2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1)+len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
