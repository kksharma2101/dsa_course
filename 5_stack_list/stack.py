#  ===== Assignment-7 Stack using List =====

# Stack is a linear data structure.
# this is working on principle is Last in First Out(LIFO)

# Operations on Stack -
# - Push = Add data
# - Pop = out data in container
# - is_empty = create a function for checking is empty and not
# - Peek = Show last data
# - Size = Show size

# === Real world example of stack ===
# - Travelling Bag
# - Compiled plates in buffet
# - Stack of books
# - Bread packet

# ==== Implemention of Stack ====
# - Using List
# - By extending list class
# - Using singly linkd list class
# - By extending singly linked list class
# - Using linked list concept

# 1. Define a class stack to implement stack data structure using list. Define __init__() method to create an empty list object as instance object member of Stack.

class Stack:
    def __init__(self):
        self.item = []

# 2. Define a method is_empty() to check if the Stack is empty in Stack class.
    def is_empty(self):
        return len(self.item) == 0
# 3. Define push method to add data into the Stack.
    def push(self, data):
        self.item.append(data)
        
# 4. Define pop method to remove top element from the Stack.
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")
            
# 5. Define a peek method to return top element from the Stack.
    def peek(self):
        return self.item[-1]

# 6. Define a size method to return size of the Stack that is number of items present in the Stack.
    def size(self):
        return len(self.item)

obj = Stack()
obj.push(49)
obj.push(70)
obj.push(55)
obj.push(21)
print("Last element is", obj.peek())
obj.pop()
print("Last element is", obj.peek())
