# task 02
# Research about "Inorder, Preorder, Postorder" and implement in DFS

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder traversal
# Inorder traversal visits the node in the order: Left -> Root -> Right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)
    else:
        return False

# Preorder traversal
# Preorder traversal visits the node in the order: Root -> Left -> Right    
def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
    else:
        return False
# Postorder traversal
# Postorder traversal visits the node in the order: Left -> Right -> Root
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")
    else:
        return False
# Creating a binary tree

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('F')

print("Inorder traversal:")
inorder_traversal(root)

print("\nPreorder traversal:")
preorder_traversal(root)

print("\nPostorder traversal:")
postorder_traversal(root)









