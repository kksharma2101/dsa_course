#  ===== Assignment-15 Deque Using Doubly Linked List Concept =====

# 1. Define a class Node with instance object member variable prev, item and next.
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

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
    def insert_front(self, data):
        n = Node(None, data, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

# 5. In deque class, define insert_rear() method to add data at the rear of the deque.
    def insert_rear(self, data):
        n = Node(self.rear, data, None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

# 6. In deque class, define delete_front() method to remove data at the front of the deque.
    def delete_front(self):
        if not self.is_empty():
            if self.front.next is None:
                return self.front == None
            else:
                self.front = self.front.next
                self.front.next.prev = None
            self.item_count -= 1

# 7. In deque class, define delete_rear() method to remove rear element at the rear of the deque.
    def delete_rear(self):
        if not self.is_empty():
            if self.rear.prev is None:
                self.rear == None
            else:
                self.rear.prev.next = None
                self.rear = self.rear.prev
            self.item_count -= 1

# 8. In deque class, define get_front() method to return front element of the deque.
    def get_front(self):
        if not self.is_empty():
            return self.front.item

# 9. In deque class, define get_rear() method to return rear element of the deque.
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item

# 10. In deque class, define size() method to return size of the deque that is number of items present in the deque.
    def size(self):
        return self.item_count

deque = Deque()
deque.insert_front(21)
deque.insert_front(31)
deque.insert_rear(41)
deque.insert_rear(51)
deque.delete_front()
deque.delete_rear()
print(deque.get_front())
print(deque.get_rear())
print(deque.size())