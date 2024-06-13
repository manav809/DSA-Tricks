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
            x = self.stack1.pop()
            self.stack2.append(x)
        res = self.stack2.pop()
        for i in range(len(self.stack2)):
            x = self.stack2.pop()
            self.stack1.append(x)
        return res
    def peek(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)):
            x = self.stack1.pop()
            self.stack2.append(x)
        res = self.stack2.pop()
        self.stack2.append(res)
        for i in range(len(self.stack2)):
            x = self.stack2.pop()
            self.stack1.append(x)
        return res

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1) == 0: return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()