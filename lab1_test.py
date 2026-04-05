import unittest
from lab1_function import arr

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(arr([1,2,4,7,10,11,7,12,6,7,16,18,19]), (3,9))
    def test2(self):
        self.assertEqual(arr([1,2,3,4,5]), (-1,-1))
    def test3(self):
        self.assertEqual(arr([5,4,3,2,1]), (0,4))
    def test4(self):
        self.assertEqual(arr([10]), (-1,-1))
    def test5(self):
        self.assertEqual(arr([1,2,3,10,0,2,3,10]), (0,6))

if __name__ == '__main__':
    unittest.main()