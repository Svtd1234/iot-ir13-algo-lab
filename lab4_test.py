import unittest
from lab4 import AVLPriorityQueue


class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.extract_max())

    def test_insert_and_extract_order(self):
        self.pq.insert("Task A", 1)
        self.pq.insert("Task B", 10)
        self.pq.insert("Task C", 5)
        self.pq.insert("Task D", 20)

        self.assertEqual(self.pq.extract_max(), ("Task D", 20))
        self.assertEqual(self.pq.extract_max(), ("Task B", 10))
        self.assertEqual(self.pq.extract_max(), ("Task C", 5))
        self.assertEqual(self.pq.extract_max(), ("Task A", 1))
        self.assertIsNone(self.pq.extract_max())

    def test_same_priority(self):
        self.pq.insert("Task 1", 5)
        self.pq.insert("Task 2", 5)

        self.assertEqual(self.pq.extract_max(), ("Task 2", 5))
        self.assertEqual(self.pq.extract_max(), ("Task 1", 5))

    def test_peek(self):
        self.pq.insert("Task A", 10)
        self.pq.insert("Task B", 20)

        self.assertEqual(self.pq.peek(), ("Task B", 20))
        self.assertEqual(self.pq.peek(), ("Task B", 20))

        self.assertEqual(self.pq.extract_max(), ("Task B", 20))
        self.assertEqual(self.pq.peek(), ("Task A", 10))


if __name__ == '__main__':
    unittest.main()