class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.curr_index = 0

    def append(self, item):
        pass

    def get(self):
        # Create array for holding items in buffer
        temp = []
        for value in self.storage:
            # for every value in the buffer then add it to temp if it is not None
            if value:
                temp.append(value)

        # return a list of the values currently in the buffer
        return temp

