class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert(start, value):
    if (start == None):
        new_node = Node(0)
        new_node.data = value
        new_node.next = new_node.prev = new_node
        start = new_node
        return start


    last = (start).prev

    new_node = Node(0)
    new_node.data = value

    new_node.next = start

    (start).prev = new_node

    new_node.prev = last

    last.next = new_node
    return start


def deleteNode(start, key):
    if (start == None):
        return None

    curr = start
    prev_1 = None
    while (curr.data != key):
        if (curr.next == start):
            print("List doesn't have node",
                  "with value = ", key)
            return start

        prev_1 = curr
        curr = curr.next

    if (curr.next == start and prev_1 == None):
        (start) = None
        return start

    if (curr == start):

        prev_1 = (start).prev

        start = (start).next

        prev_1.next = start
        (start).prev = prev_1

    elif (curr.next == start):

        prev_1.next = start
        (start).prev = prev_1

    else:

        temp = curr.next

        prev_1.next = temp
        temp.prev = prev_1

    return start


def display(start):
    temp = start

    while (temp.next != start):
        print(temp.data, end=" ")
        temp = temp.next

    print(temp.data)


if __name__ == '__main__':
    start = None

    start = insert(start, 4)
    start = insert(start, 5)
    start = insert(start, 6)
    start = insert(start, 7)
    start = insert(start, 8)

    print("List Before Deletion: ")
    display(start)

    start = deleteNode(start, 9)
    print("List After Deletion: ")
    display(start)

    start = deleteNode(start, 4)
    print("List After Deleting", 4)
    display(start)

    start = deleteNode(start, 8)
    print("List After Deleting ", 8)
    display(start)

    start = deleteNode(start, 6)
    print("List After Deleting ", 6)
    display(start)
