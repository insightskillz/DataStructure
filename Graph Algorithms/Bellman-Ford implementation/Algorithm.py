class Algorithm(object):
    HAS_CYCLE= False

    def calculateShortesPart(self, vertextList,  edgeList, startVertex):
        startVertex.minDistance = 0
        for i in range(0, len(vertextList)-1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecesor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected...")
                Algorithm.HAS_CYCLE = True
                return




