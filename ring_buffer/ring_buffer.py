class RingBuffer:
    def __init__(self, capacity):
        self.storage = []  # list for holding items
        self.capacity = capacity  # max number of items the buffer can hold
        self.curr_index = 0  # attribute for keeping track of where to add items when capacity is reached

    # Method for adding items to a Ring Buffer
    def append(self, item):
        if len(self.storage) < self.capacity:
            # if the number of items in the buffer are less than the capacity then add the item to the end
            self.storage.append(item)
        else:
            # if capacity is reached then overwrite values in the buffer with newly added items
            self.storage[self.curr_index] = item

        # calculate the new current index
        self.curr_index = (self.curr_index + 1) % self.capacity

    # Method for retrieving all the items in a RingBuffer and returning them in a list
    def get(self):
        # Create array for holding items in buffer
        temp = []
        for value in self.storage:
            # for every value in the buffer then add it to temp if it is not None
            if value:
                temp.append(value)

        # return a list of the values currently in the buffer
        return temp

