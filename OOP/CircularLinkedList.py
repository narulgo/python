class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None


def Insert(head, data):
    current = head

    newNode = Node(0)

    if (newNode == None):
        print("\nMemory Error\n")
        return None

    newNode.data = data


    if (head == None):
        newNode.next = newNode
        head = newNode
        return head

    else:
        while (current.next != head):
            current = current.next

        newNode.next = head

        current.next = newNode

    return head


def Display(head):
    current = head

    if (head == None):

        print("\nDisplay List is empty\n")
        return

    else:

        while (True):

            print(current.data, end=" ")
            current = current.next
            if (current == head):
                break;


def Length(head):
    current = head
    count = 0

    if (head == None):

        return 0

    else:
        while (True):
            current = current.next
            count = count + 1
            if (current == head):
                break;

    return count


def DeleteFirst(head):
    previous = head
    next = head


    if (head == None):
        print("\nList is empty")
        return None


    if (previous.next == previous):
        head = None
        return None

    while (previous.next != head):
        previous = previous.next
        next = previous.next


    previous.next = next.next

    head = previous.next

    return head


def DeleteLast(head):
    current = head
    temp = head
    previous = None


    if (head == None):
        print("\nList is empty")
        return None

    
    if (current.next == current):
        head = None
        return None

    
    while (current.next != head):
        previous = current
        current = current.next

    previous.next = current.next
    head = previous.next

    return head


def DeleteAtPosition(head, index):
    len = Length(head)
    count = 1
    previous = head
    next = head


    if (head == None):
        print("\nDelete Last List is empty")
        return None

    if (index >= len or index < 0):
        print("\nIndex is not Found")
        return None

    if (index == 0):
        head = DeleteFirst(head)
        return head

    while (len > 0):

        if (index == count):
            previous.next = next.next

            return head

        previous = previous.next
        next = previous.next
        len = len - 1
        count = count + 1

    return head


head = None
head = Insert(head, 99)
head = Insert(head, 11)
head = Insert(head, 22)
head = Insert(head, 33)
head = Insert(head, 44)
head = Insert(head, 55)
head = Insert(head, 66)


print("Initial List: ")
Display(head)
print("\nAfter Deleting node at index 4: ")
head = DeleteAtPosition(head, 4)
Display(head)


print("\n\nInitial List: ")
Display(head)
print("\nAfter Deleting first node: ")
head = DeleteFirst(head)
Display(head)


print("\n\nInitial List: ")
Display(head)
print("\nAfter Deleting last node: ")
head = DeleteLast(head)
Display(head)
