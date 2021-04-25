
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

        # calculate the new current index, example capacity = 4 index = 3 + 1, 4 % 4 = 0, so index goes back to start
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


rb = RingBuffer(5)  # Initialize a Ringbuffer with capacity set at 5

rb.append(7)  # 7
rb.append(14)  # 7 14
rb.append(21)  # 7 14 21
rb.append(28)  # 7 14 21 28
rb.append(35)  # 7 14 21 28 35 (Capacity met)

rb.append(42)  # 42 14 21 28 35
rb.append(49)  # 42 49 21 28 35
rb.append(56)  # 42 49 56 28 35

print(rb.get())  # Should print: [42, 49, 56, 28, 35]
