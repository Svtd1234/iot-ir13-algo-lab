import unittest
from lab3_func import is_tree_balanced, BinaryTree, get_height

class TestTreeBalance(unittest.TestCase):
    def test_example_from_task(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node(self):
        root = BinaryTree(99)
        self.assertTrue(is_tree_balanced(root))

if __name__ == '__main__':
    unittest.main()