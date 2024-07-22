# ======== Assignment-4: Doubly Linked List ==========

# If we used Doubly linked list dsa so we easily go previous node and next node.

# 1. Define a class Node to describe a node of a doubly linked list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

# Define a class DLL to implement doubly linked list with __init__() method to create and initialise start refference variable.

class DLL():
    def __init__(self, start):
        self.start = start
        
# Define a method is_empty() to checked if the linked list is empty in DLL class.
    def is_empty(self):
        return self.start == None

# Define a method inser_at_start() to insert an element at the starting of the list
    def insert_at_start(self, data ):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

# Define a method inser_at_last() to insert an element at the end of the list
    def insert_at_last(self, data):
        temp = self.start
        if temp.next != None:
            while temp.next != None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n

# Define a method search() to find the node with specified element value.
    def search(self, data):
        temp = self.start
        while temp.next != None:
            if temp.item != data:
                return temp
            temp = temp.next
        return None
        
# Define a method to print all the elements of the list.
    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
        

obj = DLL(start=None)
obj.insert_at_start(28)
obj.insert_at_start(39)
obj.insert_at_last(21)
obj.insert_at_start(55)
obj.search(21)
obj.print_all()