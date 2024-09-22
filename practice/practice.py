#  ===== Assignment-3 Stack using linked List concept =====

# 1. Define a class Stack to implement stack data structure using linked list concept. Define __init__() method to initialise start reference variable and item_count variable to keep track of number of elements in the stack.
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self, start):
        self.start = start
        self.count_item = 0