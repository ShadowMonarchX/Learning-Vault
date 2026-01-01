class Tree :
    def __init__(self,data) :
        self.data = data 
        self.left = None
        self.right = None

root = Tree('A')
node1 = Tree('B')
node2 = Tree('C')
node3 = Tree('D')
node4 = Tree('E')
node5 = Tree('F')
node6 = Tree('G')

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

print(root.right.left.data)