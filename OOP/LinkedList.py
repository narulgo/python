class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_first(self, element):
        n = Node(element)
        n.next_node = self.head
        self.head = n

    def insert_last(self, element):
        n = Node(element)
        if self.head is None:
            self.head = n
            return
        m = self.head
        while m.next_node is not None:
            m = m.next_node
        m.next_node = n

    def delete_first(self):
        n = self.head
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