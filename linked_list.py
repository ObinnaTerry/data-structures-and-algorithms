class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.count = {'len': 0}
        if nodes is not None and len(nodes) != 0:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.count['len'] += 1
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                self.count['len'] += 1
        if nodes is not None and nodes == []:
            raise Exception("Cant't create an empty head node")

    def insert_head(self, node):
        node.next = self.head
        self.head = node
        self.count['len'] += 1

    def insert_tail(self, node):
        node_ = self.head
        if not node_:
            self.head = node
            self.count['len'] += 1
            return
        while True:
            if node_.next is None:
                node_.next = node
                self.count['len'] += 1
                break
            node_ = node_.next

    def insert_after(self, target_node, new_node):
        if not self.head:
            raise Exception('List is empty')
        for node in self:
            if node.data == target_node:
                next_node = node.next
                node.next = new_node
                new_node.next = next_node
                self.count['len'] += 1
                return
        raise Exception('Target node can not be found')

    def insert_before(self, target_node, new_node):
        if not self.head:
            raise Exception('List is empty')
        if self.head.data == target_node:
            return self.insert_head(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = new_node
                new_node.next = node
                self.count['len'] += 1
                return
            prev_node = node
        raise Exception('Target node can not be found')

    def remove_node(self, target_node):
        if not self.head:
            raise Exception('Cant remove from an empty list')
        if self.head.data == target_node:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = node.next
                self.count['len'] -= 1
                return
            prev_node = node
        raise Exception('Target node can not be found')

    def reverse_list(self):
        current_node = self.head
        prev_node = None

        if self.count['len'] < 2:
            raise Exception("Cant reverse a list of length < 2")
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def __len__(self):
        return self.count['len']

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


# one = Node('a')
# two = Node('b')
# three = Node('c')
# one.next = two
# two.next = three
# llist = LinkedList()
# llist.head = one
llist = LinkedList(['a', 'b', 'c'])
# n = Node('d')
# llist.remove_node('b')
llist.reverse_list()
print(llist)
print(len(llist))
