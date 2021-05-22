import sys


class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize


class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class BellmanFord(object):
    HAS_CYCLE = False

    def calculateShortestPath(self, vertexList, edgeList, startVertex):

        startVertex.minDistance = 0

        for i in range(0, len(vertexList) - 1):
            for edge in edgeList:

                u = edge.startVertex
                v = edge.targetVertex

                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected...")
                BellmanFord.HAS_CYCLE = True
                return

    def hasCycle(self, edge):
        if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return True
        else:
            return False

    def getShortestPathTo(self, targetVertex):

        if not BellmanFord.HAS_CYCLE:
            print("Shortest path exists with value: ", targetVertex.minDistance)

            node = targetVertex

            while node is not None:
                print("%s " % node.name)
                node = node.predecessor
        else:
            print("Negative cycle detected...")


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
edge8 = Edge(2, node5, node4)

edge9 = Edge(1, node1, node2)
edge10 = Edge(1, node2, node3)
edge11= Edge(-3, node3, node1)

node1.adjacenciesList.append(edge1)
node2.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge4)
node4.adjacenciesList.append(edge5)
node4.adjacenciesList.append(edge6)
node5.adjacenciesList.append(edge7)
node5.adjacenciesList.append(edge8)

vertexList = (node1, node2, node3, node4, node5)
edgeList = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8)
#edgeList = (edge9, edge10, edge11)

algorithm = BellmanFord()
algorithm.calculateShortestPath(vertexList, edgeList, node1)
algorithm.getShortestPathTo(node2)