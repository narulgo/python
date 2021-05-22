class Node(object):
    def __init__(self,data):
        self.data = data                        
        self.nextNode = None                    


class LinkedList(object):
    def __init__(self):
        self.head = None                        
        self.size = 0                           


    def insertStart(self,data):
        self.size += 1                          
        newNode = Node(data)                    
        if not self.head:                       
            self.head = newNode                 
        else:                                   
            newNode.nextNode = self.head        
            self.head = newNode                 
        return 'Node {} added to Head of Linked List'.format(data)


    def linkedListSize(self):
        return self.size                        

    
    def linkedListSize2(self):
        actualNode = self.head                  
        size = 0                                
        while actualNode is not None:           
            size += 1                           
            actualNode = actualNode.nextNode    
        return size                             


    def insertEnd(self,data):
        self.size += 1                          
        newNode = Node(data)                    
        actualNode = self.head                  

        while actualNode.nextNode is not None:  
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode           
        return 'Node {} added to End of Linked List'.format(data)


    def removeNode(self,data):
        if self.head is None:                   
            return
        self.size -= 1
        currentNode = self.head                 
        previousNode = None                     

        while currentNode.data != data:         
            previousNode = currentNode          
            currentNode = currentNode.nextNode 

        if previousNode is None:                
            self.head = currentNode.nextNode    
        else:
            previousNode.nextNode = currentNode.nextNode    
        return 'Node {} Removed from Linked List'.format(data)


    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print('%d' % actualNode.data)
            actualNode = actualNode.nextNode


if __name__ == '__main__':

	linked_List = LinkedList()
	print(linked_List.insertStart(12))                     
	print(linked_List.insertStart(122))                    
	print(linked_List.insertStart(3))                      
	print(linked_List.insertEnd(31))                       
	linked_List.traverseList()
	print('Size of Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(31))
	print('Size of new Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(122))
	print('Size of new Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(3))
	print('Size of new Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(12))
	print('Size of new Linked List: ',linked_List.linkedListSize())
