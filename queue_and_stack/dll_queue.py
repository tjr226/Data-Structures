import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        # self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        ''' 
            dll lets us get from front and end of queue in constant time
            in this implementation - 
            enqueue to head
            dequeue from tail
        '''
        
    def enqueue(self, value):
        self.storage.add_to_head(value)
        # self.size = self.storage.length

    def dequeue(self):
        dequeued_value = self.storage.remove_from_tail()
        # self.size = self.storage.length
        return dequeued_value

    def len(self):
        return self.storage.length



