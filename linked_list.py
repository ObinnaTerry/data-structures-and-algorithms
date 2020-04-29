class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def insert_head(self, node):
        node.next = self.head
        self.head = node



    def __len__(self):
        node = self.head
        count = 0
        if node is None:
            return 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        node_list = []
        if node is None:
            return str(None)
        for i in self:
            node_list.append(i)
        return str(node_list)
        # while node is not None:
        #     node_list.append(node.data)
        #     node = node.next
        # return str(node_list)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# one = Node('a')
# two = Node('b')
# three = Node('c')
# one.next = two
# two.next = three
# llist = LinkedList()
# llist.head = one
# llist = LinkedList(['a', 'b', 'c'])
# n = Node('d')
# llist.insert_tail(n)
# print(llist)
