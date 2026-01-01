class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Liked :
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data) # this data will create a node btween store a last address of at last data in arrys
        if self.head is None: # cheak a node is empty or not empty about true this codision wille true 
            self.head = new_node
            return
        else:
            new_node.next = self.head
        self.head = new_node
    
    def inserBtween(self , data , index) :
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertEnd(self , data) :
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        current_node = self.head
        
        while(current_node.next) :
            current_node = current_node.next
        current_node.next = new_node
    
    def DeleteLastIndex(self , index) :
        
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next

    def anyindexDelete(self , index) :
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index :
            self.remove_first_node()
            return
        else :
            while(current_node.next.next):
                current_node = current_node.next

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
    def updateData(self,val,index) :
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
    def remove_node(self, data):
        current_node = self.head
 
        if current_node.data == data:
            self.remove_first_node()
            return
 
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
 

list = Liked()
print("  ")
print("Create a Like List And Inser A Numbers ")
list.insertAtBegin(1)
list.insertAtBegin(2)
list.insertAtBegin(3)
list.insertAtBegin(4)
list.insertAtBegin(5)
list.insertAtBegin(6)
list.insertAtBegin(7)
print("  ")
print("Insert Any Number Btween ")
list.inserBtween(1001,5)
print("  ")
print("Insert Any Number End ")
list.insertEnd(10)
print("  ")
print("Insert Delete Last ")
list.DeleteLastIndex(2)
print("  ")
print("Insert First Number")
list.remove_first_node()
print("  ")
print("Insert Any Number Btween ")
list.DeleteLastIndex(4)
print("  ")
print("\nUpdate node Value\n")
list.updateData(1111, 0)
print("  ")
print("\nremove node with Value\n")
list.remove_node(3)
list.printLL()
print("  ")
print("\nSize of linked list :", end=" ")
print(list.size())