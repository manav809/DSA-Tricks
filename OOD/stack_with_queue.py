class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        top = None
        for i in range(len(self.queue1)): 
            front = self.queue1.pop(0)
            if self.queue1 == []: 
                top = front
                continue
            self.queue2.append(front)

        for i in range(len(self.queue2)): 
            front = self.queue2.pop(0)
            self.queue1.append(front)
        return top

    def top(self):
        """
        :rtype: int
        """
        top = None
        for i in range(len(self.queue1)): 
            front = self.queue1.pop(0)
            if self.queue1 == []: 
                top = front
            self.queue2.append(front)
        for i in range(len(self.queue2)): 
            front = self.queue2.pop(0)
            self.queue1.append(front)
        return top        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue1 == []: return True
        else: return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()