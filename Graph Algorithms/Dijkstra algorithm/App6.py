from Vertex import Vertex
from Edge import Edge
from Dijkstraalgorithm import Algorithm

node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(1, node1, node2)
edge2 = Edge(1,node2, node3)
edge3 = Edge(0.1, node1, node3)

node1.adjacentList.append(edge1)
node2.adjacentList.append(edge2)
node3.adjacentList.append(edge3)

vertexList = {node1,node2, node3}
algorithm = Algorithm()
algorithm.calculateShortestPath(vertexList, node1)
algorithm.getShortextPathTo(node3)