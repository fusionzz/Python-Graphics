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
        return "x:" + self.x + " y:" + self.y + " z:"

class Edge:
    def __init__(self, start: Node, stop: Node) -> None:
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

class Wirefram:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def addNode(self, node: Node) -> None:
        for listNode in self.nodes:
            if listNode == node:
                print(node + " is already in the wireframe")
                return

        self.nodes.append(Node(node))

    def addNodes(self, nodes: list[Node]) -> None:
        for node in nodes:
            self.addNode(node)

    def addEdge(self, edge: Edge) -> None:
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

        if not start:
            self.addNode(Node(start))
        if not stop:
            self.addNode(Node(stop))
        
        #once confirmed both nodes are in, checks that edge is not duplicate
        for listEdge in self.edges:
            if listEdge == edge:
                print(edge + " is already in wireframe")
                return

        self.edges.append(edge)

    def addEdges(self, edges: list[Edge]) -> None:
        for edge in edges:
            self.addEdge(Edge(edge))