class Node:
    def __init__(self, coordinates: list[float]) -> None:
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

    #compare two nodes for equality
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            raise TypeError(other + " is not a node,")

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
            raise TypeError(other + " is not an edge.")
        
        #edges are bidirectional
        return (self.start == other.start and self.stop == other.stop) or (self.start == other.stop and self.stop == other.start)
    
    def __str__(self) -> str:
        return str(self.start) + " to " + str(self.stop)

class Wireframe:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def printEdges(self) -> str:
        edge_str = "Edges:\n"
        for edge in self.edges:
            edge_str += str(edge) + "\n"
        return edge_str

    def printNodes(self) -> str:
        node_str = "Nodes:\n"
        for node in self.nodes:
            node_str += str(node) + "\n"
        return node_str

    def __str__(self) -> str:
        return self.printNodes() + self.printEdges()


    def addNode(self, node: Node) -> None:
        for listNode in self.nodes:
            if listNode == node:
                print(str(node) + " is already in the wireframe")
                return

        self.nodes.append(node)

    def addNodes(self, nodes: list[Node]) -> None:
        for node in nodes:
            self.addNode(node)

    def addEdge(self, edge: Edge) -> None:
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

    def addEdges(self, edges: list[Edge]) -> None:
        for edge in edges:
            self.addEdge(edge)