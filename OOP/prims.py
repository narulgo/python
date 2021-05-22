import heapq


class Vertex():

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []

    def __str__(self):
        return self.name


class Edge():

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

    def __lt__(self, other):
        selfPriority = self.weight;
        otherPriority = other.weight;
        return selfPriority < otherPriority;


class PrimsJarnik():

    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.edgeHeap = []
        self.fullCost = 0

    def calculateSpanningTree(self, vertex):
        self.unvisitedList.remove(vertex);
        while self.unvisitedList:

            for edge in vertex.adjacencyList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge);

            minEdge = heapq.heappop(self.edgeHeap);

            if minEdge.targetVertex in self.unvisitedList:
                self.spanningTree.append(minEdge)
                print("Edge added to spanning tree: %s - %s" % (minEdge.startVertex.name, minEdge.targetVertex.name))
                self.fullCost += minEdge.weight
                vertex = minEdge.targetVertex
                self.unvisitedList.remove(vertex)

    def getSpanningTree(self):
        return self.spanningTree

    def getCost(self):
        return self.fullCost


vertex1 = Vertex("1")
vertex2 = Vertex("2")
vertex3 = Vertex("3")
vertex4 = Vertex("4")
vertex5 = Vertex("5")
vertex6 = Vertex("6")

edge12 = Edge(2, vertex1, vertex2)
edge21 = Edge(2, vertex2, vertex1)
edge15 = Edge(4, vertex1, vertex5)
edge51 = Edge(4, vertex5, vertex1)
edge14 = Edge(1, vertex1, vertex4)
edge41 = Edge(1, vertex4, vertex1)
edge23 = Edge(3, vertex2, vertex3)
edge32 = Edge(3, vertex3, vertex2)
edge24 = Edge(3, vertex2, vertex4)
edge42 = Edge(3, vertex4, vertex2)
edge26 = Edge(7, vertex2, vertex6)
edge62 = Edge(7, vertex6, vertex2)
edge34 = Edge(5, vertex3, vertex4)
edge43 = Edge(5, vertex4, vertex3)
edge36 = Edge(8, vertex3, vertex6)
edge63 = Edge(8, vertex6, vertex3)
edge45 = Edge(9, vertex4, vertex5)
edge54 = Edge(9, vertex5, vertex4)

unvisitedList = []
unvisitedList.append(vertex1)
unvisitedList.append(vertex2)
unvisitedList.append(vertex3)
unvisitedList.append(vertex4)
unvisitedList.append(vertex5)
unvisitedList.append(vertex6)


vertex1.adjacencyList.append(edge12)
vertex2.adjacencyList.append(edge21)
vertex1.adjacencyList.append(edge15)
vertex5.adjacencyList.append(edge51)
vertex1.adjacencyList.append(edge14)
vertex4.adjacencyList.append(edge41)
vertex2.adjacencyList.append(edge23)
vertex3.adjacencyList.append(edge32)
vertex2.adjacencyList.append(edge24)
vertex4.adjacencyList.append(edge42)
vertex2.adjacencyList.append(edge26)
vertex6.adjacencyList.append(edge62)
vertex3.adjacencyList.append(edge34)
vertex4.adjacencyList.append(edge43)
vertex3.adjacencyList.append(edge36)
vertex6.adjacencyList.append(edge63)
vertex4.adjacencyList.append(edge45)
vertex5.adjacencyList.append(edge54)

algorithm = PrimsJarnik(unvisitedList)
algorithm.calculateSpanningTree(vertex5)
print(algorithm.getCost())