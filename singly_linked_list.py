# A linked list a data structure, used for fast and memory efficient insertions and deletions.
# Unlike arrays, which are single objects, linked lists contain multiple 'node' objects
# that are linked together via references.

# Linked lists can either be singly or doubly linked.

# 1. A Node object, which contains the data for the element, as well as a reference to the next Node in the list.
# 2. A LinkedList object, which holds all of the objects in the list

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

    # method that prints the list so we can see what we have created
    def to_string(self):
        # current is set equal to the Head node
        current = self.head
        return_string = "HEAD"
        # iterate over our Linked List until current is none
        while(current != None):
            return_string += ' > ' + str(current.data)
            # then set the current node equal to the next node
            next_node = current.next
            current = next_node
        return return_string + " > None "




new_list = LinkedList()

new_list.insert_front('foo')
print(new_list.to_string())
# HEAD > foo > None

new_list.insert_front('bar')
print(new_list.to_string())
# HEAD > bar > foo > None

new_list.insert_front('meh')
print(new_list.to_string())
# HEAD > meh > bar > foo > None

new_list.insert_front('baz')
print(new_list.to_string())
# HEAD > baz > meh > bar > foo > None

new_list.insert_end('wee')
print(new_list.to_string())
# HEAD > baz > meh > bar > foo > wee > None

new_list.insert_end('baa')
print(new_list.to_string())
# HEAD > baz > meh > bar > foo > wee > baa > None

new_list.delete_end()
print(new_list.to_string())
# HEAD > baz > meh > bar > foo > wee > None

new_list.delete_front()
print(new_list.to_string())
# HEAD > meh > bar > foo > wee > None
