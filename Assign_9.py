#  ===== Assignment-11 Stack implementation by extending Sll =====

# 1. Import module containing singly linked list code in your python file.
from Assign_1 import *

# 2. Define a class Stack to implement stack data structure by inheriting SLL class.
class Stack(SLL): # SLL is parent of Stack class there is the inheritance
    def __init__(self):
        super().__init__()
        self.count = 0
# 3. Define a method is_empty() to check if the Stack is empty in Stack class.
    def is_empty(self):
        return super().is_empty()

# 4. Define push method to add data into the Stack.
    def push(self, data):
        self.insert_at_start(data)
        self.count += 1

# 5. Define pop method to remove top element from the Stack.
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.count -= 1
        else:
            raise IndexError('Stack is empty')

# 6. Define a peek method to return top element from the Stack.
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Stack is empty')

# 7. Define a size method to return size of the Stack that is number of items present in the Stack.
    def size(self):
        return self.count

obj = Stack()
obj.push(21)
obj.push(41)
obj.push(51)
print(obj.size())
print(obj.peek())