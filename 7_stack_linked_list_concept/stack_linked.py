#  ===== Assignment-3 Stack using linked List concept =====

# 1. Define a class Stack to implement stack data structure using linked list concept. Define __init__() method to initialise start reference variable and item_count variable to keep track of number of elements in the stack.
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        
# 2. Define a method is_empty() to check if the Stack is empty in Stack class.
    def is_empty(self):
        return self.top == None
    
# 3. Define push method to add data into the Stack.
    def push(self, data):
        n=Node(data, self.top)
        self.top = n
        self.count += 1
        
# 4. Define pop method to remove top element from the Stack.
    def pop(self):
        if not self.is_empty():
            data=self.top.item
            self.top=self.top.next
            self.count -= 1
            return data
        else:
            raise IndexError("Stack is empty")
        
# 5. Define a peek method to return top element from the Stack.
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            IndexError("Stack is empty")

# 6. Define a size method to return size of the Stack that is number of items present in the Stack.
    def size(self):
        return self.count
    
linked_stack=Stack()
linked_stack.push(45)
linked_stack.push(21)
linked_stack.pop()
print("Stack size is", linked_stack.size())
print("Top element is",linked_stack.peek())