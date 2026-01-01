class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add1(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

# Example usage:
my_list1 = LinkedList()

my_list2 = LinkedList()

my_list1.add1(5)
my_list1.add1(6)
my_list1.add1(7)

my_list2.add1(2)
my_list2.add1(1)
my_list2.add1(4)


# Printing the list elements

x3 = []
x4 = []
current1 = my_list1.head
current2 = my_list2.head
while current1:
    x1 = [current1.value]
    x3.extend(x1)
    current1 = current1.next

while current2 :
    x2 = [current2.value]
    x4.extend(x2)
    current2 = current2.next

print(x3)
print(x4)

