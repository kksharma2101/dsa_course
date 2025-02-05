#  ===== Assignment-15 Deque Using Doubly Linked List Concept =====

# 1. Define a class Node with instance object member variable prev, item and next.
class Node:
    def __init__(self, prev, item, next):
        self.prev = None
        self.item = None
        self.next = None

# 2. Define a class Deque to implement queue data structure using doubly linked List concept. Define __init__() method to initialise front and rear reference variable, and item_count() variable to keep track of number of elements in the deque.
class Deque:
    def __init__(self):
            self.front = None
            self.rear = None
            self.item_count = 0

# 3. Define a method is_empty() to check if the deque is empty in deque class.
    def is_empty(self):
         return self.front == None

# 4. In deque class, define insert_front() method to add data at the front of the deque.
    def insert_front(self,data):
        n = Node(data)
        self.dll.insert_at_start(n)