import numpy as np
        
class Wireframe:
    def __init__(self) -> None:
        #creates numpy array with 0 rows and 4 columns, last column for transforms
        #ex: x y z 1
        self.nodes = np.zeros((0,4), dtype=int)
        self.edges = []

    def strNode(self, node) -> str:
        return f"x:{node[0]} y:{node[1]} z:{node[2]}"

    def strNodes(self) -> str:
        node_str = "Nodes:\n"
        i = 0
        for node in self.nodes:
            node_str += f"Node {i}: " + self.strNode(node) + "\n"
            i += 1
        return node_str
    
    def strEdge(self, edge):
        return f"{edge[0]} -> {edge[1]}"
    
    def strEdges(self) -> str:
        edge_str = "Edges:\n"
        i = 0
        for edge in self.edges:
            edge_str += f"Edge {i}: " + self.strEdge(edge) + "\n"
            i += 1
        return edge_str
    
    def printEdges(self) -> None:
        print(self.strEdges())

    def printNodes(self) -> None:
        print(self.printNodes())

    def __str__(self) -> str:
        return self.strNodes() + self.strEdges()


    def addNode(self, node: np.ndarray) -> None:
        #checks for numpy array
        if not isinstance(node, np.ndarray):
            raise TypeError("Can only add numpy array to nodes")
        #checks that node is correct size
        if node.shape != (3,):
            raise ValueError("Node is not the correct size")
        
        #addes ones column to node
        ones_column = np.ones((1,), dtype=int)
        ones_added = np.hstack((node, ones_column))

        #checks for duplicate nodes
        if ones_added.tolist() in self.nodes.tolist():
            print(self.strNode(node) + " is already in the wireframe")
            return

        #adds nodes to list of nodes
        self.nodes = np.vstack((self.nodes, ones_added))

    def addNodes(self, nodes: np.ndarray) -> None:
        #checks for numpy array
        if not isinstance(nodes, np.ndarray):
            raise TypeError("Can only add numpy array to nodes")
        
        for node in nodes:
            self.addNode(node)

    def addEdge(self, edge: list) -> None:
        #checks for proper edges
        if not isinstance(edge, list):
            raise TypeError("Please provide a list of 2 nodes")
        if len(edge) != 2:
            raise ValueError("Please use a list of only 2 nodes")
        if (not isinstance(edge[0], int)) or (not isinstance(edge[1], int)):
            raise TypeError("List indices must be integers")
        if edge[0] < 0 or edge[1] < 0 or edge[0] >= len(self.nodes) or edge[1] >= len(self.nodes):
            raise ValueError("List indices out of bounds")
        if edge[0] == edge[1]:
            raise ValueError("Edge cannot be between 2 of the same node")

        #checks for duplicate edge
        if edge in self.edges or edge[::-1] in self.edges:
            print(self.strEdge(edge) + " is already in the wireframe")
            return
        
        self.edges.append(edge)

    def transform(self, matrix: np.ndarray) -> None:
        """applies transformation matrix to all nodes"""
        self.nodes = np.dot(self.nodes, matrix)

    def translationMatrix(dx=0, dy=0, dz=0) -> np.ndarray:
        """returns translation matrix"""
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [dx, dy, dz, 1]
        ])

    def addEdges(self, edges: list) -> None:
        for edge in edges:
            self.addEdge(edge)

    def findCenter(self) -> list:
        """Finds center of wireframe"""
        num_nodes = self.nodes.shape[0]
        mean_x = sum([node[0] for node in self.nodes]) / num_nodes
        mean_y = sum([node[1] for node in self.nodes]) / num_nodes
        mean_z = sum([node[2] for node in self.nodes]) / num_nodes

        return [mean_x, mean_y, mean_z]

    def scaleMatrix(sx=0, sy=0, sz=0) -> np.ndarray:
        """Return matrix for scaling along all axis around center"""

        return np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])
    
    def toCenterAndBack(self, matrix):
        """translates object to center, applies transformation matrix, translates back"""
        center_coords = self.findCenter()
        self.transform(Wireframe.translationMatrix(*[-x for x in center_coords]))
        self.transform(matrix)
        self.transform(Wireframe.translationMatrix(*center_coords))

    
    def autoScale(self, sx=0, sy=0, sz=0) -> None:
        scaleMatrix = Wireframe.scaleMatrix(sx, sy, sz)
        self.toCenterAndBack(scaleMatrix)


    def rotateXMatrix(radians):
        c = np.cos(radians)
        s = np.sin(radians)

        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ])
    
    def rotateYMatrix(radians):
        c = np.cos(radians)
        s = np.sin(radians)

        return np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ])
    
    def rotateZMatrix(radians):
        c = np.cos(radians)
        s = np.sin(radians)

        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
    def rotateX(self, radians):
        rotateMatrix = Wireframe.rotateXMatrix(radians)
        self.toCenterAndBack(rotateMatrix)

    def rotateY(self, radians):
        rotateMatrix = Wireframe.rotateYMatrix(radians)
        self.toCenterAndBack(rotateMatrix)

    def rotateZ(self, radians):
        rotateMatrix = Wireframe.rotateZMatrix(radians)
        self.toCenterAndBack(rotateMatrix)