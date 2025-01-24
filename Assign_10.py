#  ===== Assignment-12 Queue Using List =====

# Note - Queue is linear data structure [FIFO]
# Question - [1. Using list, 2. by extending list class, 3. Using singly linked list class, 4. by extending singly linked list class, 5. using linked list concept]

# 1. Define a class queue to implement queue data structure using list. Define __init__() method to create an empty list object as instance object member of queue.
class Queue:
    def __init__(self):
        self.mylist = []

# 2. Define a method is_empty() to check if the Queue is empty in Queue class.
    def is_empty(self):
        return len(self.mylist) == 0

# 3. In Queue class, define enqueue method to add data at the rear end of the queue.
    def enqueue(self, item):
        self.mylist.append(item)

# 4. In Queue class, define dequeue method to remove front element from the queue.
    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop(0)
        else: 
            raise IndexError('List is empty')

# 5. In Queue class, define get_front() method to return front element from the queue.
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            return None

# 6. In Queue class, define get_rear() method to return rear element from the queue.
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[len(self.mylist)-1]
        else:
            return None

# 7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.
    def size(self):
        if not self.is_empty():
            return len(self.mylist)
        else:
            pass




obj = Queue()
obj.enqueue(21)
obj.enqueue(11)
obj.enqueue(61)
# obj.dequeue()
print(obj.get_front(), end='front ')
print(obj.get_rear(), end='rear ')
print(obj.size())
obj.is_empty()
print(obj.mylist)

