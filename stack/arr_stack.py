class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        # self.size = len(self.storage)

    def pop(self):
        if self.size > 0:
            result = self.storage.pop()
            # self.size = len(self.storage)
            self.size -= 1
            return result
