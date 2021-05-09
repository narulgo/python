class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_first(self, element):
        n = Node(element)
        if self.head is None:
            self.head = self.tail = n
        else:
            n.next_node = self.head
            self.head = n

    def insert_last(self, element):
        n = Node(element)
        if self.head is None:
            self.head = self.tail = n
        else:
            self.tail.next_node = n
            self.tail = n

    def delete_first(self):
        n = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = n.next_node
            n.next_node = None
        return n.element

    def print_list(self):
        n = self.head
        print("[", end=' ')
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print("]")


# ll = LinkedList()
# ll.insert_first(30)
# ll.insert_first(4)
# ll.insert_first(13)
# ll.insert_first(3)
# ll.insert_first(5)
# ll.print_list()
# ll.insert_last(9)
# ll.print_list()
# ll.delete_first()
# ll.print_list()
# print(ll.is_empty())