class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bst_search(root, target) -> bool:
    while root is not None:
        if target == root.value:
            return True
        elif target < root.value:
            # идем в левое поддерево
            root = root.left
        else:
            # идем в правое поддерево
            root = root.right
    
    return False

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)

print(bst_search(root, 6)) # True
print(bst_search(root, 7)) # False
print(bst_search(root, 14)) # True