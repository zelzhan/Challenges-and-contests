class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min:
            if x < self.min[-1]:
                self.min.append(x)
            elif x >= self.min[-1]:
                self.min.append(self.min[-1])
        else:
            self.min.append(x)
        self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.min.pop()
            self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]
        
        

    def getMin(self):
        """
        :rtype: int
        """
        
        if self.min:
            return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
