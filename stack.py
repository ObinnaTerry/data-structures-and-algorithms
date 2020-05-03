class Stack:

    def __init__(self, size=None):
        self.size = size if size is not None else 100
        self.stack = [None] * self.size  # initialize an empty list of length size
        self.top = -1

    def push(self, num):
        if self.top == self.size - 1:
            raise Exception("Error: Stack Overflow")
        self.top += 1
        self.stack[self.top] = num
        return
