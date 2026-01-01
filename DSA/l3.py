class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printData(head):
    if not head:
        print("null")
        return

    current_node = head
    while True:
        print(current_node.data, end="->")
        current_node = current_node.next
        if current_node == head:
            break
    print("(back to head)")

def deleteNode(head, node_delete):
    if not head:
        return None

    if head == node_delete and head.next == head:
        return None

    current_node = head
    prev_node = None

    while True:
        if current_node == node_delete:
            if prev_node:
                prev_node.next = current_node.next
            else:
                last_node = head
                while last_node.next != head:
                    last_node = last_node.next
                head = current_node.next
                last_node.next = head
            return head
        prev_node = current_node
        current_node = current_node.next
        if current_node == head:
            break

    return head

def updateNode(head, node_update, value):
    if not head:
        return None

    current_node = head
    while True:
        if current_node == node_update:
            current_node.data = value
            return head
        current_node = current_node.next
        if current_node == head:
            break

    return head

def insertNode(head, value, position):
    new_node = Node(value)
    if not head:
        new_node.next = new_node
        return new_node

    if position == 0:
        last_node = head
        while last_node.next != head:
            last_node = last_node.next
        new_node.next = head
        last_node.next = new_node
        return new_node

    current_node = head
    count = 0
    while current_node.next != head and count < position - 1:
        current_node = current_node.next
        count += 1

    new_node.next = current_node.next
    current_node.next = new_node

    return head

def sortList(head):
    if not head or head.next == head:
        return head

    nodes = []
    current_node = head
    while True:
        nodes.append(current_node.data)
        current_node = current_node.next
        if current_node == head:
            break

    nodes.sort()

    current_node = head
    for data in nodes:
        current_node.data = data
        current_node = current_node.next

    return head

def findElement(head, value):
    if not head:
        print(f"Element {value} does not exist in the list.")
        return

    current_node = head
    while True:
        if current_node.data == value:
            print(f"Element {value} exists in the list.")
            return
        current_node = current_node.next
        if current_node == head:
            break

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
n6.next = n1

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
