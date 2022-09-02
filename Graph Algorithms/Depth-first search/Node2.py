class Node(object):
    def __int__(self, name):
        self.name = name
        self.adjacentList = []
        self.visited = False
