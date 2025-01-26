#  ===== Assignment-13 Queue Using Singly Linked List concept =====

# 1. Define a class queue to implement queue data structure using SLL concept. Define __init__() method to initialise front and rear reference variable, and item_count() variable to keept track of number of elements in the queue.
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

# 2. Define a method is_empty() to check if the Queue is empty in Queue class.
    def is_empty(self):
        return self.front == 0

# 3. In Queue class, define enqueue method to add data into the queue.
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            # self.rear = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

# 4. In Queue class, define dequeue method to remove front element from the queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

# 5. In Queue class, define get_front() method to return front element from the queue.
    def get_front(self):
        if not self.is_empty():
            return self.front.item

# 6. In Queue class, define get_rear() method to return rear element from the queue.
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError('Queue is empty')

# 7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.
    def size(self):
        if not self.is_empty():
            print(self.front)
            print(self.rear)
            return self.item_count

q1 = Queue()
q1.enqueue(33)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print('front = ', q1.get_front())
print('rear = ', q1.get_rear())
# q1.dequeue()
print(q1.size())