from functools import singledispatchmethod

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
    