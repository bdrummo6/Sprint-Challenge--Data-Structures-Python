class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # Function reverses item order in a singly linked list
    def reverse_list(self, node, prev):
        # if node is not none proceed with reversing the list
        if node:
            # Retrieve the initial value of the second node in the list
            current = self.head.get_next()
            # set the next reference of head to prev
            self.head.set_next(prev)
            # store the head reference in prev
            prev = self.head

            # if the next reference for head is None then return the new head of the reversed list
            if not current:
                return self.head
            # if the next reference is not None, keep moving through the list
            else:
                self.head = current

            # if the list reversal is not complete then recursively call reverse_list
            return self.reverse_list(node, prev)

    def print_list(self):
        current = self.head
        while current:
            print(current.get_value())
            current = current.get_next()

ll = LinkedList()

ll.add_to_head(5)
ll.add_to_head(8)
ll.add_to_head(17)
ll.add_to_head(25)
ll.add_to_head(13)
ll.add_to_head(14)

print('\nNon-reversed List: ')
ll.print_list()

ll.reverse_list(Node(), None)

print('\nReversed List: ')
ll.print_list()