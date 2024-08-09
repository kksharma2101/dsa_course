# Assignment-6: Circular Doubly Linked List

# 1. Define a class Node to describe a node of a circular doubly linked list.
class Node:
    def __init__(self, pre = None, item = None, next = None):
        self.pre = pre
        self.item = item
        self.next = next

# 2. Define a class CDLL to implement circular doubly linked list with __init__() method to create and initialise last refference variable.
class Cdll:
    def __init__(self, start = None):
        self.start = start

# 3. Define a method is_empty() to check if the linked list is empty in CDLL class.
    def is_empty(self):
        return self.start == None

# 4. Define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, data):
        n=Node(None, data)
        if self.start == None:
            n.next = n
            n.pre = n
        else:
            n.next = self.start
            n.pre = self.start.pre
            self.start.pre.next = n
            # self.start.pre = n
        self.start = n

# 5. Define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, data):
        n = Node(None, data)
        if self.start == None:
            n.next = n
            n.pre = n
            self.start = n
        else:
            n.next = self.start
            n.pre = self.start.pre
            self.start.pre.next = n
            self.start.pre = n
        
# 6. Define a method search() to find the node with specified element value.
    def search(self, data):
        pass

# 8. Define a method to print_all() the elements of the list.
    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item)
                temp = temp.next
            print(temp.item)

cdll_obj = Cdll()
cdll_obj.insert_at_start(43)
cdll_obj.insert_at_start(76)
cdll_obj.insert_at_last(21)
cdll_obj.insert_at_last(35)
cdll_obj.print_list()