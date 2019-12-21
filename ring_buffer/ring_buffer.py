from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # appends item to ring buffer
        # if ring buffer is full, oldest element is overwritten by newest one
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail 

        elif self.current is self.storage.tail:
            self.storage.delete(self.storage.head)
            self.storage.add_to_head(item)
            self.current = self.storage.head
        
        else:
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)

    def get(self):
        # Note:  This is the only [] allowed
        # returns all of the elements in the buffer in a list in their given order
        list_buffer_contents = []          
        current = self.storage.head 
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        if self.current < self.capacity - 1:
            self.current += 1
        else: 
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]

