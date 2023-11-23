class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)): 
            top = self.stack1.pop()
            self.stack2.append(top)
        value = self.stack2.pop()
        for j in range(len(self.stack2)): 
            top = self.stack2.pop()
            self.stack1.append(top)
        return value
    def peek(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)): 
            top = self.stack1.pop()
            self.stack2.append(top)
        value = self.stack2.pop()
        self.stack2.append(value)
        for j in range(len(self.stack2)): 
            top = self.stack2.pop()
            self.stack1.append(top)
        return value       

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack1 == []: return True
        else: return False 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()