class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

from collections import deque

def bfs(root):
    if not root:
        return
    
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("BFS Tranversal: ")
bfs(root)