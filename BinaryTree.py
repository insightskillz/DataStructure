class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)

        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

        def insertRight(self, newNode):
            if self.right == None:
                self.right = BinaryTree(newNode)

            else:
                temp = BinaryTree(newNode)
                temp.right = self.right
                self.right = temp

    def insertInBinaryTree(root, data):
        newNode = BinaryTree(data)
        if root is None:
            root = newNode
            return root
