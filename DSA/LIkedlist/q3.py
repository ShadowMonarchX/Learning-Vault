# Create a Node class to create a node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertAtBegin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node

	

	def remove_at_index(self, index):
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



	def printLL(self):
		current_node = self.head
		while(current_node):
			print(current_node.data)
			current_node = current_node.next


# create a new linked list
llist = LinkedList()


llist.insertAtBegin('c')
llist.insertAtBegin('a')
llist.insertAtBegin('b')
llist.insertAtBegin('w')
llist.insertAtBegin('p')


# print the linked list
print("Node Data")
llist.printLL()

print("Remove Node at Index 1")
llist.remove_at_index(1)
llist.printLL()

