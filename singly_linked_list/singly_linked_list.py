#  Assignment-3 Singly linked list
# Define a class Node to describe a node of a Singly Linked List

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

# Define a class SLLL to implement Singly linked list with __init__() method to create and initialise start reference variable

class SLL:
    def __init__(self, start):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(data, self.start)
        self.start = n
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
                temp.next = n
        else:
            self.start = n