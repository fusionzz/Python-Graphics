import unittest
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from wireframe import Edge, Node

class TestNode(unittest.TestCase):
    def test_init(self):
        start = Node([1, 2, 3])
        stop = Node([2, 3, 4])
        edge = Edge(start, stop)
        self.assertEqual(str(edge), "x:1 y:2 z:3 to x:2 y:3 z:4")

    def test_bad_init(self):
        start = Node([1, 2, 3])
        stop = Node([1, 2, 3])
        self.assertRaises(ValueError, Edge, start, stop)

    def test_eq(self):
        start = Node([1, 2, 3])
        stop = Node([2, 3, 4])
        edge1 = Edge(start, stop)
        edge2 = Edge(start, stop)
        self.assertEqual(True, edge1 == edge2)

    def test_eq_2(self):
        start = Node([1, 2, 3])
        stop = Node([2, 3, 4])
        edge1 = Edge(start, stop)
        edge2 = Edge(stop, start)
        self.assertEqual(True, edge1 == edge2)
    
    def test_not_eq(self):
        start = Node([1, 2, 3])
        stop = Node([2, 3, 4])
        start2 = Node([1, 1, 1])
        edge1 = Edge(start, stop)
        edge2 = Edge(start2, stop)
        self.assertEqual(False, edge1 == edge2)


if __name__ == '__main__':
    unittest.main()