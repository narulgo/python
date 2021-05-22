import sys
import heapq

class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize

    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

class Algorithm(object):
    def calculateShortestPath(self, vertexList, startVertex):
        q = []
        startVertex.minDistance = 0
        heapq.heappush(q, startVertex)
        while q:
            actualVertex = heapq.heappop(q)
            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(q, v)

    def getShortestPathTo(self, targetVertex):
        print("Shortest path to vertex is: ", targetVertex.minDistance)
        node = targetVertex
        while node is not None:
            print("%s " % node.name)
            node = node.predecessor


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")


edge1 = Edge(6, node1, node3)
edge2 = Edge(3, node2, node1)
edge3 = Edge(6, node1, node4)
edge4 = Edge(2, node3, node4)
edge5 = Edge(1, node4, node3)
edge6 = Edge(1, node4, node2)
edge7 = Edge(4, node5, node2)
edge8 = Edge(9, node5, node4)

node1.adjacenciesList.append(edge1)
node2.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge4)
node4.adjacenciesList.append(edge5)
node4.adjacenciesList.append(edge6)
node5.adjacenciesList.append(edge7)
node5.adjacenciesList.append(edge8)

vertexList = (node1, node2, node3, node4, node5)

algorithm = Algorithm()
algorithm.calculateShortestPath(vertexList, node1)
algorithm.getShortestPathTo(node2)