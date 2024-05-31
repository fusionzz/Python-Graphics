from functools import singledispatchmethod
import math

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

class Wireframe:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def strEdges(self) -> str:
        edge_str = "Edges:\n"
        for edge in self.edges:
            edge_str += str(edge) + "\n"
        return edge_str

    def strNodes(self) -> str:
        node_str = "Nodes:\n"
        for node in self.nodes:
            node_str += str(node) + "\n"
        return node_str
    
    def printEdges(self) -> None:
        edge_str = "Edges:\n"
        for edge in self.edges:
            edge_str += str(edge) + "\n"
        print(edge_str)

    def printNodes(self) -> None:
        node_str = "Nodes:\n"
        for node in self.nodes:
            node_str += str(node) + "\n"
        print(node_str)

    def __str__(self) -> str:
        return self.strNodes() + self.strEdges()


    def addNode(self, node: Node) -> None:
        #checks for node object
        if not isinstance(node, Node):
            raise TypeError("Can only add Node object to nodes")
        
        for listNode in self.nodes:
            if listNode == node:
                print(str(node) + " is already in the wireframe")
                return

        self.nodes.append(node)

    def addNodes(self, nodes: list[Node]) -> None:
        for node in nodes:
            self.addNode(node)

    @singledispatchmethod
    def addEdge(self, edge: Edge) -> None:
        #checks for edge object
        if not isinstance(edge, Edge):
            raise TypeError("Can only add Edge object to edges")

        #confirm not a dupe edge
        for listEdge in self.edges:
            if listEdge == edge:
                print(str(edge) + " is already in the wireframe")
                return

        #check that nodes are in wireframe before adding edge
        start = edge.start
        stop = edge.stop
        checkStart = False
        checkStop = False
        for node in self.nodes:
            if start == node:
                checkStart = True
            if stop == node:
                checkStop = True
        
        #can raise error if node is not in nodes, or can just add it in
        # if not start:
        #     raise ValueError(start + " is not in the wireframe, please add it first")
        # if not stop:
        #     raise ValueError(stop + " is not in the wireframe, please add it first")

        if not checkStart:
            self.addNode(start)
        if not checkStop:
            self.addNode(stop)

        self.edges.append(edge)
    
    @addEdge.register(list)
    def _(self, edge: list[int]) -> None:
        #checks that each edge has only 2 nodes
        if len(edge) != 2:
            raise ValueError("Please provide only 2 node indices")
        
        #checks that node indices are in bound
        if edge[0] >= len(self.nodes) or edge[1] >= len(self.nodes) or edge[0] < 0 or edge[1] < 0:
            raise ValueError("Index out of bounds")
        
        self.edges.append(Edge(self.nodes[edge[0]], self.nodes[edge[1]]))

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
            d = math.hypot(y, x)
            theta = math.atan2(y, x) + radians
            node.x = center_x + d * math.cos(theta)
            node.y = center_y + d * math.sin(theta)

    def rotateX(self, center:list[float], radians:float) -> None:
        """rotate on x axis around center by radians"""

        center_x, center_y, center_z = center

        for node in self.nodes:
            z = node.z - center_z
            y = node.y - center_y
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            node.z = center_z + d * math.cos(theta)
            node.y = center_y + d * math.sin(theta)

    def rotateY(self, center:list[float], radians:float) -> None:
        """rotate on y axis around center by radians"""

        center_x, center_y, center_z = center

        for node in self.nodes:
            x = node.x - center_x
            z = node.z - center_z
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            node.x = center_x + d * math.sin(theta)
            node.z = center_z + d * math.cos(theta)


