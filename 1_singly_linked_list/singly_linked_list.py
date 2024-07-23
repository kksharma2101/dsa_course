#  Assignment-3 Singly linked list

# Singly linked list work only forward (accending oder) direction, if we want to back so we will start , start node.

# Define a class Node to describe a node of a Singly Linked List

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

# Define a class SLLL to implement Singly linked list with __init__() method to create and initialise start reference variable

class SLL:
    def __init__(self, start):
        self.start = start

# Define a method is_empty() to checked if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start == None

# Define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

# Define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

# Define a method search() to find the node with specified element value.
    def search(self, item):
        temp = self.start
        while temp.next is not None:
            if temp.item == item:
                return temp
            temp = temp.next
        return None

# Define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

# Define a method to print_all() the elements of the list.
    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next

# Define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

# Define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            return None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
        temp.next = None

# Define a method delete_item() to delete specified element from the list.
    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    
    def __iter__(self):
        return SLLIterator(self.start)
                        
# Implement for iterator for SLL to access all the elements of list in a sequence.
class SLLIterator():
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

result = SLL(start=None)

result.insert_at_start(10)
result.insert_at_start(30)
result.insert_at_start(50)
result.insert_at_last(20)
result.insert_after(result.search(30),40)
# result.delete_first()
# result.delete_last()
# result.print_all()
result.print_all()
result.delete_item(30)
print(" ")
# print(result.print_all());
for x in result:
    print(x)