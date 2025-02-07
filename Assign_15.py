#  ===== Assignment-17 Priority Queue Using Linked List =====

# 1. Define a Node class with instance member variables item, priority and next.
class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next

# 2. Define a class PriorityQueue to implement priority queue data structure usnig linked list. provide __init__() method to create a start reference variable (initially containing None) and item_count variable (initialy 0).
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

# 3. Define a push() method in PriorityQueue class to insert new data with given priority.
    def push(self, data, priority):
        n=Node(data, priority)
        if not self.start or self.start.priority > priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

# 4. Define a is_empty() method in PriorityQueue class to check if the priority queue is empty.
    def is_empty(self):
        return self.start == None

# 5. Define a pop() method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception is priority queue is empty.
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data


# 6. In class PriorityQueue, Define a method size to return the number of elements present in the priority queue.
    def size(self):
        return self.item_count

psl = PriorityQueue()
psl.push('kumar3',3)
psl.push('kumar2',2)
psl.push('kumar1',1)
print(psl.pop())
print(psl.pop())
print(psl.size())