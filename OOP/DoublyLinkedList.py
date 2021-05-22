class Node(object):
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def Insert(self, value):
        newNode = Node(value, None, None)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def traverse(self):
        currentNode = self.head
        while currentNode:
            item_val = currentNode.value
            currentNode = currentNode.next
            yield item_val

    def printList(self):
        for node in self.traverse():
            print(node)

    def search(self, val):
        for node in self.traverse():
            if val == node:
                return True
        return False

    def delete(self, value):
        currentNode = self.head
        node_deleted = False
        if currentNode is None:
            node_deleted = False

        elif currentNode.value == value:
            self.head = currentNode.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while currentNode:
                if currentNode.value == value:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                    node_deleted = True
                currentNode = currentNode.next

        if node_deleted:
            self.count -= 1


items = doubly_linked_list()
items.Insert('PHP')
items.Insert('Python')
items.Insert('C#')
items.Insert('C++')
items.Insert('Java')
items.Insert('SQL')

print("Original list:")
items.printList()
items.delete("Java")
print("\nList after deleting two items:")
items.printList()
print(items.search("Python"))