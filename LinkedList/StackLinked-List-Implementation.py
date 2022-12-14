# Modification made to the code

class Node:
    def __init__(self):
        self.data = None
        self.next = None
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None


class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()

our_list = ["First", "second", "Third", "Fourth"]
our_stack = Stack(our_list)
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())
print(our_stack.pop())