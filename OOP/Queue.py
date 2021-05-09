from LinkedList import *

class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def is_empty(self):
        return self.queue.is_empty()

    def enqueue(self, element):
        self.queue.insert_last(element)

    def dequeue(self):
        return self.queue.delete_first()

    def print_queue(self):
        self.queue.print_list()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print_queue()
while not q.is_empty():
    q.dequeue()
q.print_queue()