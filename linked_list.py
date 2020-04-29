class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        node_list = []
        if node is None:
            return 'List is empty'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
