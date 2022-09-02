import sys

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visted = False
        self.adjacentList = []
        self.predecessor = None
        self.minDistance = sys.maxsize



    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

