import unittest
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from wireframe import Wireframe
from io import StringIO
import numpy as np


class TestWireframeClass(unittest.TestCase):
    def setUp(self):
        self.wireframe = Wireframe()
        """
        self.wireframe.addNode(Node([1, 2, 3]))
        self.wireframe.addNodes([Node([2, 2, 2]), Node([1, 1, 1])])
        self.wireframe.addEdge(Edge(Node([1, 1, 1]), Node([2, 2, 2])))
        """
        self.wireframe.addNode(np.array([1, 2, 3]))
        self.wireframe.addNodes(np.array([[2, 2, 2], [1, 1, 1]]))
        self.wireframe.addEdge([2, 1])
    
    def tearDown(self):
        del self.wireframe

    def test_init(self):
        wf_str = "Nodes:\nNode 0: x:1 y:2 z:3\nNode 1: x:2 y:2 z:2\nNode 2: x:1 y:1 z:1\nEdges:\nEdge 0: 2 -> 1\n"
        self.assertEqual(wf_str, str(self.wireframe))

    def test_add_node(self):
        #self.wireframe.addNode(Node([3, 3, 3]))
        self.wireframe.addNode(np.array([3, 3, 3]))
        wf_str = "Nodes:\nNode 0: x:1 y:2 z:3\nNode 1: x:2 y:2 z:2\nNode 2: x:1 y:1 z:1\nNode 3: x:3 y:3 z:3\nEdges:\nEdge 0: 2 -> 1\n"
        self.assertEqual(wf_str, str(self.wireframe))

    def test_add_dupe_node(self):
        capturedOutput= StringIO()
        sys.stdout = capturedOutput
        self.wireframe.addNode(np.array([1, 2, 3]))
        sys.stdout = sys.__stdout__
        self.assertEqual("x:1 y:2 z:3 is already in the wireframe\n", capturedOutput.getvalue())

    def test_add_edge(self):
        #self.wireframe.addEdge(Edge(Node([1, 2, 3]), Node([1, 1, 1])))
        self.wireframe.addEdge([0, 2])
        wf_str = "Nodes:\nNode 0: x:1 y:2 z:3\nNode 1: x:2 y:2 z:2\nNode 2: x:1 y:1 z:1\nEdges:\nEdge 0: 2 -> 1\nEdge 1: 0 -> 2\n"
        self.assertEqual(wf_str, str(self.wireframe))
    """
        #DEPRACATED
        def test_add_edge_node_indices(self):
        self.wireframe.addEdge([0, 1])
        wf_str = wf_str = "Nodes:\nx:1 y:2 z:3\nx:2 y:2 z:2\nx:1 y:1 z:1\nEdges:\nx:1 y:1 z:1 to x:2 y:2 z:2\nx:1 y:2 z:3 to x:2 y:2 z:2\n"
        self.assertEqual(wf_str, str(self.wireframe))
    """

    def test_add_dupe_edge(self):
        capturedOutput= StringIO()
        sys.stdout = capturedOutput
        #self.wireframe.addEdge(Edge(Node([1, 1, 1]), Node([2, 2, 2])))
        self.wireframe.addEdge([2, 1])
        sys.stdout = sys.__stdout__ 
        self.assertEqual("2 -> 1 is already in the wireframe\n", capturedOutput.getvalue())

    def test_add_dupe_reverse_edge(self):
        capturedOutput= StringIO()
        sys.stdout = capturedOutput
        #self.wireframe.addEdge(Edge(Node([1, 1, 1]), Node([2, 2, 2])))
        self.wireframe.addEdge([1, 2])
        sys.stdout = sys.__stdout__ 
        self.assertEqual("1 -> 2 is already in the wireframe\n", capturedOutput.getvalue())
    
    """
    #DEPRACATED
    def test_add_edge_no_node_start(self):
        self.wireframe.addEdge(Edge(Node([3, 3, 3]), Node([1, 2, 3])))
        wf_str = "Nodes:\nx:1 y:2 z:3\nx:2 y:2 z:2\nx:1 y:1 z:1\nx:3 y:3 z:3\nEdges:\nx:1 y:1 z:1 to x:2 y:2 z:2\nx:3 y:3 z:3 to x:1 y:2 z:3\n"
        self.assertEqual(wf_str, str(self.wireframe))
    
    def test_add_edge_no_node_stop(self):
        self.wireframe.addEdge(Edge(Node([1, 2, 3]), Node([3, 3, 3])))
        wf_str = "Nodes:\nx:1 y:2 z:3\nx:2 y:2 z:2\nx:1 y:1 z:1\nx:3 y:3 z:3\nEdges:\nx:1 y:1 z:1 to x:2 y:2 z:2\nx:1 y:2 z:3 to x:3 y:3 z:3\n"
        self.assertEqual(wf_str, str(self.wireframe))
    """

if __name__ == '__main__':
    unittest.main()