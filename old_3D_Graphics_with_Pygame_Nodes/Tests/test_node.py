import unittest
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from wireframe import Node

class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node([1, 2, 3])
        self.assertEqual(str(node), "x:1 y:2 z:3")

    def test_eq(self):
        node = Node([1,2,3])
        self.assertEqual(node == Node([1,2,3]), True)
    
    def test_not_eq(self):
        node = Node([1,2,3])
        self.assertEqual(node == Node([1,2,4]), False)


if __name__ == '__main__':
    unittest.main()