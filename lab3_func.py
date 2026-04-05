class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_height(node):
    if node is None:
        return 0

    left_h = get_height(node.left)
    right_h = get_height(node.right)

    if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
        return -1

    return max(left_h, right_h) + 1

def is_tree_balanced(node):
    return get_height(node) != -1

