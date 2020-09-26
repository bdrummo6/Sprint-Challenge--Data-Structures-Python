
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        # Compare the new value with the parent node
        if self.value:
            # if value is less than the current parent node value
            if value < self.value:
                # if there is no left child node then a new node with the value is inserted to the left
                if not self.left:
                    self.left = new_node
                # if there is a left child node then insert is called on the left child node
                else:
                    self.left.insert(value)
            # if value is greater than or equal to the current parent node value
            elif value >= self.value:
                # if there is no right child node then a new node with the value is inserted to the right
                if not self.right:
                    self.right = new_node
                # if there is a right child node then insert is called on the right child node
                else:
                    self.right.insert(value)
        # if the root node of the BST is None then the new value is assigned to the root node's value
        else:
            self.value = value

    # Return True if the tree contains the value and False if it does not
    def contains(self, target):
        if not self:
            return False
        # if the target value is less than current parent node's value
        if target < self.value:
            # if there is no left child node then the BST does not contain the target value
            if not self.left:
                return False
            # if there is a left child node then contains is called on the left child node
            return self.left.contains(target)
        # if the target value is greater than or equal to the current parent node's value
        elif target > self.value:
            # if there is no right child node then the BST does not contain the target value
            if not self.right:
                return False
            # if there is a right child node then contains is called on the right child node
            return self.right.contains(target)
        # target value is equal to the current node value
        else:
            return True
