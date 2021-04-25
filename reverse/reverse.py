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

    # Function using iteration reverses node order in a singly linked list
    def reverse_list(self, node, prev):
        if node:
            current = self.head  # Set current to head for iterating through the linked list
            # Loop while current is not None
            while current:
                next = current.get_next()  # Store a reference to the second node in the list in a variable next
                current.set_next(prev)  # Store the current's next reverence to prev
                prev = current  # Set prev with the reference to current
                current = next  # Set the node referenced by next to current

            self.head = prev  # This sets the last node to of the non-reversed list to the head of the new reversed list

    """
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
    """

    def print_list(self):
        current = self.head
        while current:
            print(current.get_value())
            current = current.get_next()


# Created Linked list to run my own tests on the reverse_list function
ll = LinkedList()

ll.add_to_head(5)  # 5
ll.add_to_head(8)  # 8 5
ll.add_to_head(17)  # 17 8 5
ll.add_to_head(25)  # 25 17 8 5
ll.add_to_head(13)  # 13 25 17 8 5
ll.add_to_head(14)  # 14 13 25 17 8 5

print('\nNon-reversed List: ')
ll.print_list()  # Linked List should be: 14 13 25 17 8 5

ll.reverse_list(Node(), None)  # Call reverse list with an Empty Node and prev set as None

print('\nReversed List: ')
ll.print_list()  # Linked List should be: 5 8 17 25 13 24
