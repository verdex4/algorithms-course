class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root, result):
    # root -> left -> right
    if root is None:
        return
    result.append(str(root.value))
    preorder(root.left, result)
    preorder(root.right, result)

def inorder(root, result):
    # left -> root -> right
    if root is None:
        return
    inorder(root.left, result)
    result.append(str(root.value))
    inorder(root.right, result)

def postorder(root, result):
    # left -> right -> root
    if root is None:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(str(root.value))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

preorder_result = []
inorder_result = []
postorder_result = []

preorder(root, preorder_result)
inorder(root, inorder_result)
postorder(root, postorder_result)

print("preorder:", " ".join(preorder_result)) # 2 1 3
print("inorder:", " ".join(inorder_result)) # 1 2 3
print("postorder:", " ".join(postorder_result)) # 1 3 2