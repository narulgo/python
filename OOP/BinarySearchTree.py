class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterativeSearch(root, key):
    while root != None:
        if key > root.data:
            root = root.right
        elif key < root.data:
            root = root.left
        else:
            return True
    return False

def insert(Node, data):
    if Node == None:
        return newNode(data)
    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)
    return Node

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    if iterativeSearch(root, 80):
        print("Yes")
    if iterativeSearch(root,20):
        print("20 is available")
    else:
        print("No")