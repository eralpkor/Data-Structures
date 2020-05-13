# without helper
class ArrQueue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add to tail, back of the queue
        self.storage.append(value)
        self.size += 1
        # self.size = len(self.storage)

    def dequeue(self):
        # remove and return at the front of the queue
        if self.size < 1:
            return None

        result = self.storage.pop(0)
        self.size -= 1
        return result
