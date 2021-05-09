from LinkedList import * 

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, element):
        self.stack.insert_first(element)
    
    def pop(self):
        return self.stack.delete_first()

    def print_stack(self):
        self.stack.print_list()

s = Stack()
print(s.is_empty())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print_stack()
s.pop()
s.print_stack()