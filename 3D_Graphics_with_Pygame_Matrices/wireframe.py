import numpy as np

"""
class Node:
    def __init__(self, coordinates: list[float]) -> None:
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

    #compare two nodes for equality
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            raise TypeError(str(other) + " is not a node,")

        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self) -> str:
        return "x:" + str(self.x) + " y:" + str(self.y) + " z:" + str(self.z)

"""

"""
class Edge:
    def __init__(self, start: Node, stop: Node) -> None:
        if start == stop:
            raise ValueError("Start and stop nodes cannot be the same")
        self.start = start
        self.stop = stop

    #compare two edges for equality
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            raise TypeError(str(other) + " is not an edge.")
        
        #edges are bidirectional
        return (self.start == other.start and self.stop == other.stop) or (self.start == other.stop and self.stop == other.start)
    
    def __str__(self) -> str:
        return str(self.start) + " to " + str(self.stop)
"""
        
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
        
        #OLD checks for duplicate nodes
        """
        for listNode in self.nodes:
            if (listNode == node).all():
                print(str(node) + " is already in the wireframe")
                return
        """
        
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
        

    def addEdges(self, edges: list) -> None:
        for edge in edges:
            self.addEdge(edge)

    def findCenter(self) -> list[float]:
        """Find the center of the wireframe"""

        num_nodes = len(self.nodes)
        mean_x = sum([node.x for node in self.nodes]) / num_nodes
        mean_y = sum([node.y for node in self.nodes]) / num_nodes
        mean_z = sum([node.z for node in self.nodes]) / num_nodes

        return (mean_x, mean_y, mean_z)
    
    def translate(self, axis:str, d:int) -> None:
        """Translates each node of wireframe by d along given axis"""

        if axis in ['x', 'y', 'z']:
            for node in self.nodes:
                setattr(node, axis, getattr(node, axis) + d)
        else:
            raise ValueError("Please enter valid axis")

    def scale(self, center_coords:list, scale:float) -> None:
        """Scale the wireframe from the center of the screen"""

        if len(center_coords) != 2:
            raise ValueError("Please provide x,y center coords")

        center_x = center_coords[0]
        center_y = center_coords[1]
        #center_z = center_coords[2]

        for node in self.nodes:
            node.x = center_x + scale * (node.x - center_x)
            node.y = center_y + scale * (node.y - center_y)
            node.z *= scale

    def autoScale(self, scale:float) -> None:
        center_coords = self.findCenter()

        center_x, center_y, center_z = center_coords

        for node in self.nodes:
            node.x = center_x + scale * (node.x - center_x)
            node.y = center_y + scale * (node.y - center_y)
            node.z *= center_z + scale * (node.z - center_z)


    """
    TO ROTATE AROUND AXIS:
    convert other 2 coords to cartesian plane, aka hypotenuse and angle
    then add angle of rotation and convert back
    https://www.petercollingridge.co.uk/tutorials/3d/pygame/rotation/
    """

    def rotateZ(self, center:list[float], radians:float) -> None:
        """rotate on z axis around center by radians"""

        center_x, center_y, center_z = center

        for node in self.nodes:
            x = node.x - center_x
            y = node.y - center_y
            d = np.hypot(y, x)
            theta = np.arctan2(y, x) + radians
            node.x = center_x + d * np.cos(theta)
            node.y = center_y + d * np.sin(theta)

    def rotateX(self, center:list[float], radians:float) -> None:
        """rotate on x axis around center by radians"""

        center_x, center_y, center_z = center

        for node in self.nodes:
            z = node.z - center_z
            y = node.y - center_y
            d = np.hypot(y, z)
            theta = np.arctan2(y, z) + radians
            node.z = center_z + d * np.cos(theta)
            node.y = center_y + d * np.sin(theta)

    def rotateY(self, center:list[float], radians:float) -> None:
        """rotate on y axis around center by radians"""

        center_x, center_y, center_z = center

        for node in self.nodes:
            x = node.x - center_x
            z = node.z - center_z
            d = np.hypot(x, z)
            theta = np.arctan2(x, z) + radians
            node.x = center_x + d * np.sin(theta)
            node.z = center_z + d * np.cos(theta)


