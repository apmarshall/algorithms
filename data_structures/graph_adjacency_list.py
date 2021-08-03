class EdgeNode:
    def __init__(self, edge, weight, nextNode):
        self.edge = edge
        self.weight = weight
        self.nextNode = nextNode
        
class Graph:
    def __init__(self, edges, degree, nedges: int, directed: bool):
        self.edges = edges
        self.degree = degree
        self.nedges = nedges
        self.directed = directed
    
    def insertEdge(graph: Graph, x, y, directed: bool):
        edgeNode = EdgeNode(y, null, edges(x))
        graph.edges[x] = edgeNode + graph.edges[x]
        graph.degree[x]++
        if directed == False:
            insertEdge(graph, y, x, True)
        else:
            graph.nedges++
    