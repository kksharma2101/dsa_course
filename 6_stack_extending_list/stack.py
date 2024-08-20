#  ===== Assignment-3 Stack extending List =====

# 1. Define a class stack to implement stack data structure by extending list class.
from typing import SupportsIndex


class Stack(list):
# 2. Define a method is_empty() to check if the Stack is empty in Stack class.
    def is_empty(self):
        return len(self) == 0

# 3. Define push method to add data onto the Stack.
    def push(self, data):
        self.append(data)
        
# 4. Define pop method to remove top element from the Stack.
    def pop(self):
        if not self.is_empty():
            super().pop() # super is the represent of parent class, because of parent class has already pop() method.

# 5. Define a peek method to return top element from the Stack.
    def peek(self):
        if not self.is_empty():
            return self[-1]

# 6. Define a size method to return size of the Stack that is number of items present in the Stack.
    def size(self):
        return len(self)

# 7. Implement a way to restrict use of insert() method of list class from stack object.
    def insert(self, index, data) -> None:
        raise AttributeError("No attribute `insert` in stack")

extendStack = Stack()
# extendStack.insert(0,19)
extendStack.push(55)
extendStack.push(21)
# extendStack.pop()
print("Top value is",extendStack.peek())
print("Total length",extendStack.size())