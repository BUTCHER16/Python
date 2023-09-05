class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Treenode(1)
root.left=Treenode(2)
root.right=Treenode(3)
root.left.left=Treenode(4)
root.left.right=Treenode(5)
root.right.left=Treenode(6)
root.right.right=Treenode(7)

def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.value, end=" ")
        inOrder(node.right)
def preOrder(node):
    if node:
        print(node.value, end=" ")
        preOrder(node.left)
        preOrder(node.right)
def PostOrder(node):
    if node:
        PostOrder(node.left)
        PostOrder(node.right)
        print(node.value, end=' ')        

print("Inorder Traversal: ")
inOrder(root)
print("\nPreOrder Traversal: ")
preOrder(root)
print("\nPostOrder Traversal: ")
PostOrder(root)