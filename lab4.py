class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def extract_max(self):
        if not self.root:
            return None
        res = self.peek()
        self.root = self._delete_leftmost(self.root)
        return res

    def peek(self):
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return (curr.value, curr.priority)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _insert(self, node, value, priority):
        if not node:
            return Node(value, priority)
        elif priority >= node.priority:
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and priority >= node.left.priority:
            return self._right_rotate(node)
        if balance < -1 and priority < node.right.priority:
            return self._left_rotate(node)
        if balance > 1 and priority < node.left.priority:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and priority >= node.right.priority:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def _delete_leftmost(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_leftmost(node.left)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance < -1:
            b_right = self._get_balance(node.right)
            if b_right <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        return node