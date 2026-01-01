class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sorted :
    def __init__(self) :
        self.head = None
    
    #def Liked(self , data):
        #new_node = Node(data)
        #if self.head == Node :
            #self.head = new_node
            #return
        #else :                                                                     
            #new_node.next = self.head
        #self.head = new_node

    def PrintAll(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def Sorted(self , data) :
        new_node = Node(data)
        current_node = self.head
        if (current_node is None or current_node.data >= new_node.data):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            
list = Sorted()
print("\n")
list.Sorted(100)
list.Sorted(10)
list.Sorted(120)
list.Sorted(0)
list.Sorted(220)
list.Sorted(210)
list.Sorted(11)
list.PrintAll()