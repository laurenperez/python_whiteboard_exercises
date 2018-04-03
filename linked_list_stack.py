
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #### method for adding a new Node to the front of the list
    def insert_front(self, data):
        # create a new Node with data
        new_node = Node(data)
        # point new node to linked list head
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    #### method for adding a new Node to the end of the list
    def insert_end(self, data):
        new_node = Node(data)
        # if there is no tail, there is one node, it will be head and tail
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            # update the tail Node's pointer to be the new node
            old_tail.next = new_node
            # update the LinkedList's tail to be the new node
            self.tail = new_node

    #### method for deleting a Node from the front of the list
    def delete_front(self):
        item_to_delete = self.head
        self.head = item_to_delete.next
        del item_to_delete

    #### method for deleting a Node from the end of the list
    def delete_end(self):
        current = self.head
        item_to_delete = self.tail
        while current.next != self.tail:
            next_node = current.next
            current = next_node
        current.next = None
        del item_to_delete
        self.tail = current


# a queue is a FIRST in LAST out structure. FILO


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, data):
        # put a thing on
        self.insert_front(data)

    def pop(self, data):
        # take the first thing off
        self.delete_front(data)



































# end
