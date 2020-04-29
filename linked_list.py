class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        node_list = []
        if node is None:
            return 'List is empty'


