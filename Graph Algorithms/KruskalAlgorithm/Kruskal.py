from DisjointSet import DisJointSet

class Algorithm(object):
    def construstSpanningTree(self, vertexList, edgeList):
        disjointSet = DisJointSet(vertexList)

        spanningTree = []
        edgeList.sort()

        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex

            if disjointSet.find(u.parentNode) is not disjointSet.find(v.parentNode):
                spanningTree.append(edge)
                disjointSet.union(u.parentNode, v.parentNode)
        for edge in spanningTree:
            print(edge.startVertex.name, " ", edge.targetVertex.name)

