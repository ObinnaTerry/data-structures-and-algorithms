class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __len__(self):
        node = self.head
        count = 0
        if node is None:
            return 0
        while node is not None:
            count += 1
            node = node.next
        return count

    

    def __repr__(self):
        node = self.head
        node_list = []
        if node is None:
            return str(None)
        while node is not None:
            node_list.append(node.data)
            node = node.next
        return str(node_list)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList(['a', 'b', 'c', 'd'])
print(len(llist))
