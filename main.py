# This is an example of a Python implemetation of a stack using OOP

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def pop(self):
        if self.head is None:
            return None
        else:
            node = self.tail
            self.tail = node.prev
            self.tail.next = None
            self.size -= 1
            return node.data
    
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.tail.data
    
    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            node = self.head
            string = ""
            while node is not None:
                string += str(node) + " "
                node = node.next
            return string