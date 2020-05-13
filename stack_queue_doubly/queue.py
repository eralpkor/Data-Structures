"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""
from doubly_linked_list import DoublyLinkedList
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add to tail, back of the queue
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # remove and return at the front of the queue
        if self.size < 1:
            return None
        self.size -= 1
        return self.storage.remove_from_head()  
        