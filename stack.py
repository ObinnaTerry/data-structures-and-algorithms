class StackArray:

    def __init__(self, size=None):
        self.size = size if size is not None else 100
        self.stack = [None] * self.size  # initialize an empty list of length size
        self.top_ = -1

    def push(self, num):
        if self.top_ == self.size - 1:
            raise Exception("Error: Stack Overflow")
        self.top_ += 1
        self.stack[self.top_] = num
        return

    def pop(self):
        if self.top_ == -1:
            raise Exception("Error: Stack is empty")
        value = self.stack[self.top_]
        self.top_ -= 1
        return value

    def top(self):
        return self.stack[self.top_]

    def is_empty(self):
        return True if self.top_ == -1 else False

    def __repr__(self):
        return str(self.stack[:self.top_ + 1])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class StackLinkedList:

    def __init__(self):
        self.head = None

    def push(self, node):
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            raise Exception("Error: Stack is empty")
        next_node = self.head.next
        value = self.head
        self.head = next_node
        return value

    def top(self):
        return self.head

    def is_empty(self):
        return True if self.head is None else False



stack = StackArray()
d = StackArray()
g = StackLinkedList()
n = Node('a')
k = Node('b')
g.push(n)
g.push(k)
# stack.pop()
stack.push(3)
stack.push(7)
stack.push(32)
# d.push(4)
print(d.is_empty())
print(stack)
print(g.is_empty())
