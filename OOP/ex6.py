class Stack(object):
    def __init__(self):
        self.array = []
    def push(self, value):
        self.array.append(value)
    def pop(self):
        top = self.array.pop()
        return top
    def top(self):
        return self.array[-1]
stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.pop()
print(stack.top())