#  ===== Assignment-16 Priority Queue Using List =====
# ***** Implimentation of priority queue *****
# 1 - Using Linked List Concept
# 2 - Using List
# 3 - Using Heap

# 1. Define a class PriorityQueue to implement priority queue data structure using list. Provide __init__() method to create a list object (initially empty).
class PriorityQueue:
    def __init__(self):
        self.items = []

# 2. Define is_empty methon in priorityQueue class to check if the priorityQueue is empty.
    def is_empty(self):
        return len(self.items) == 0

# 3. Define a push method in PriorityQueue class to insert new data with given priority.
    def push(self, priority, data):
        index = 0
        while index < len(self.items) and self.items[index][0] <= priority:
            index += 1
        self.items.insert(index, (priority, data))

# 4. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('PriorityQueue is empty')
        return self.items.pop(0)[1]

# 5. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.
    def size(self):
        return len(self.items)

pri = PriorityQueue()
pri.push(2, "Ram")
pri.push(1, "Shyam")
pri.push(6, "kamal")
pri.push(5, "sharma")
pri.push(3, "Ganesh")
pri.push(4, "Hari")

while not pri.is_empty():
    print(pri.pop())
print(pri.size())