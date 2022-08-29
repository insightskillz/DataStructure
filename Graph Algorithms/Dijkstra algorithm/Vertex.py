import sys


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacentList = []
        self.minDistance = sys.maxsize
    def __cmp__(self, otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __lt__(self, other):
        self.Priority = self.minDistance
        otherPriority = other.minDistance
        return self.Priority < otherPriority