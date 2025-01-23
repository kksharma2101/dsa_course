# ======== Assignment-4: Doubly Linked List ==========

# If we used Doubly linked list dsa so we easily go previous node and next node.

# 1. Define a class Node to describe a node of a doubly linked list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

# Define a class DLL to implement doubly linked list with __init__() method to create and initialise start refference variable.

class DLL():
    def __init__(self, start):
        self.start = start
        
# Define a method is_empty() to checked if the linked list is empty in DLL class.
    def is_empty(self):
        return self.start == None

# Define a method inser_at_start() to insert an element at the starting of the list
    def insert_at_start(self, data ):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

# Define a method inser_at_last() to insert an element at the end of the list
    def insert_at_last(self, data):
        temp = self.start
        if temp != None:
            while temp.next != None:
                temp = temp.next
        n=Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n
                
# Define a method search() to find the node with specified element value.
    def search(self, data):
        temp = self.start
        while temp.next != None:
            if temp.item != data:
                return temp
            temp = temp.next
        return None
    
# Define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, temp, data):
        if temp != None:
            n=Node(temp, data, temp.next)
            if temp.next != None:
                temp.next.pre = n
            temp.next = n
        
# Define a method to print all the elements of the list.
    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next
            
# Define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.start != None:
            self.start = self.start.next
            if self.start != None:
                self.start.prev = None
            
# Define a method delete_last() to delete first element from the list.
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

# Define a method delete_item() to delete specified element from the list.
    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item is data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

    # Second method to delete item

        # elif self.start.next is None:
        #     self.start = None
        # else:
        #     temp = self.start
        #     if temp.item == data:
        #         self.start = temp.next
        #         temp.next.prev = None
        #     else:
        #         while temp is not None:
        #             if temp.item == data:
        #                 if temp.next is None:
        #                     temp.prev.next = None
        #                 else:
        #                     temp.next.prev = temp.prev
        #                     temp.prev.next = temp.next
        #                 break        
        #             temp = temp.next
       
    def __iter__(self):
        return DLLIterator(self.start)
    
       
class DLLIterator:
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
               

obj = DLL(start=None)
obj.insert_at_start(28)
obj.insert_at_start(39)
obj.insert_at_last(21)
obj.insert_at_start(55)
# print(obj.search(21))
for x in obj:
    print(x, end=' ')
obj.insert_after(obj.search(39 | 55), 102)
# obj.print_all()
# obj.delete_first()
# obj.delete_last()
obj.delete_item(39)
print(" ")
# obj.print_all()