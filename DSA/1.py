class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLiked :
    def __init__(self) :
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node
    def Delete(self , index):
        if self.head == None :
            return
       
        current_node = self.head
        position = 0 
        if position == index:
            list.first_node()
            return
        else :
            while(current_node.next.next):
                current_node.next = current_node.next.next
            current_node.next = current_node.next.next
            
    
    def first_node(self) :
        if self.head == None :
            return
        
        self.head = self.head.next

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print()

list = DoublyLiked()
list.insertAtBegin(1)
list.insertAtBegin(122)
list.insertAtBegin(0)
list.insertAtBegin(10)
list.insertAtBegin(1222)
list.insertAtBegin(19)
print("\n")
list.first_node()
print("\n")
#list.Delete(2)
list.display()