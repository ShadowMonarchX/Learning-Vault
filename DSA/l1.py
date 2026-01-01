class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printData(head):
    current_node = head
    while current_node:
        print(current_node.data, end="->")
        current_node = current_node.next
    print("null")

def deleteNode(head, node_delete):
    if head == node_delete:
        return head.next

    current_node = head
    while current_node.next:
        if current_node.next == node_delete:
            current_node.next = current_node.next.next
            return head
        current_node = current_node.next

    return head

def updateNode(head, node_update, value):
    if head == node_update:
        head.data = value
        return head

    current_node = head
    while current_node:
        if current_node == node_update:
            current_node.data = value
            return head
        current_node = current_node.next

    return head

def insertNode(head, value, position):
    new_node = Node(value)
    if position == 0:
        new_node.next = head
        return new_node

    current_node = head
    count = 0
    while current_node and count < position - 1:
        current_node = current_node.next
        count += 1

    if current_node:
        new_node.next = current_node.next
        current_node.next = new_node

    return head

def sortList(head):
    if not head or not head.next:
        return head

    nodes = []
    current_node = head
    while current_node:
        nodes.append(current_node.data)
        current_node = current_node.next

    nodes.sort()

    current_node = head
    for data in nodes:
        current_node.data = data
        current_node = current_node.next

    return head

def findElement(head, value):
    current_node = head
    while current_node:
        if current_node.data == value:
            print(f"Element {value} exists in the list.")
            return
        current_node = current_node.next

    print(f"Element {value} does not exist in the list.")

n1 = Node(3)
n2 = Node(5)
n3 = Node(4)
n4 = Node(7)
n5 = Node(8)
n6 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

printData(n1)
n1 = deleteNode(n1, n2)
printData(n1)
n1 = updateNode(n1, n3, 6)
printData(n1)
n1 = insertNode(n1, 9, 2)
printData(n1)
n1 = sortList(n1)
printData(n1)
findElement(n1, 7)
findElement(n1, 11)