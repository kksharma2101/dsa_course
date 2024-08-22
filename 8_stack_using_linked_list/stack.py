#  ===== Assignment-3 Stack using linked List =====

# 1. Import module containing singly linked list code in your python file.
# from singly_linked_list import * # Import module again *****


# 2. Define a class Stack to implement stack data structure using linked list concept. Define __init__() method to create Singly Linked List (Sll) object.
class Stack:
    def __init__(self):
        self.my_list = SLL()
        self.count = 0

# 3. Define a method is_empty() to check if the Stack is empty in Stack class.
    def is_empty(self):
        return self.my_list.is_empty()
    
# 4. Define push method to add data into the Stack.
    def push(self, data):
        self.my_list.insert_at_start(data)
        self.count += 1
        
# 5. Define pop method to remove top element from the Stack.
    def pop(self):
        if not self.is_empty():
            self.my_list.delete_first()
            self.count -= 1
        
# 6. Define a peek method to return top element from the Stack.
    def peek(self):
        if not self.is_empty():
            return self.my_list.start.item
        
# 7. Define a size method to return size of the Stack that is number of items present in the Stack.
    def size(self):
        return self.count

stack = Stack()
stack.push(45)
stack.push(91)
stack.push(21)
print(stack.peek())
print(stack.size())