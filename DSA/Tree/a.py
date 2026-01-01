class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_height(node):
    if node is None:
        return -1  
    
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    
   
    return max(left_height, right_height) + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    
    height = find_height(root)
    print("Height of the binary tree is:", height)
