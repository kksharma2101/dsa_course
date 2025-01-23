# Assignment-6: Circular Doubly Linked List

# 1. Define a class Node to describe a node of a circular doubly linked list.
class Node:
    def __init__(self, pre = None, item = None, next = None):
        self.pre = pre
        self.item = item
        self.next = next

# 2. Define a class CDLL to implement circular doubly linked list with __init__() method to create and initialise last refference variable.
class Cdll:
    def __init__(self, start = None):
        self.start = start

# 3. Define a method is_empty() to check if the linked list is empty in CDLL class.
    def is_empty(self):
        return self.start == None

# 4. Define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, data):
        n=Node(None, data)
        if self.start == None:
            n.next = n
            n.pre = n
        else:
            n.next = self.start
            n.pre = self.start.pre
            self.start.pre.next = n
            # self.start.pre = n
        self.start = n

# 5. Define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, data):
        n = Node(None, data)
        if self.start == None:
            n.next = n
            n.pre = n
            self.start = n
        else:
            n.next = self.start
            n.pre = self.start.pre
            self.start.pre.next = n
            self.start.pre = n
        
# 6. Define a method search() to find the node with specified element value.
    def search(self, data):
        if self.start == None:
            pass
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
        return None
    
# 7. Define a method insert_after() to insert a new node after a given node of the list.
    def insert_item(self, temp, data):
        n = Node(temp, data, temp.next)
        if temp != None:
            temp.next = n
            temp.next.pre = n

# 8. Define a method to print_all() the elements of the list.
    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item)
                temp = temp.next
            print(temp.item)

# 9. Define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.start == None:
            pass
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.pre.next = self.start.next
            self.start.next.pre = self.start.pre
            self.start = self.start.next

# 10. Define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.start == None:
            pass
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.pre.pre.next = self.start
            self.start.pre = self.start.pre.pre
            
# 10. Define a method delete_item() to specified element from the list.
    def delete_item(self, data):
        if not self.is_empty():
            if self.start.next == self.start:
                if self.start.item == data:
                    self.start = None
            else:
                if self.start.item == data:
                    self.delete_first()
                else:
                    temp = self.start
                    while temp.next != self.start:
                        if temp == self.start.pre:
                            if temp.item == data:
                                self.delete_last()
                                break
                        if temp.item == data:
                            temp.next.pre = temp.pre
                            temp.pre.next = temp.next
                            break
                        temp = temp.next
           
                        
    def __iter__(self):
        return CdllIterator(self.start)

class CdllIterator:
    def __init__(self, start):
        self.current = start
        self.count = 0
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data

cdll_obj = Cdll()
cdll_obj.insert_at_start(43)
cdll_obj.insert_at_start(76)
cdll_obj.insert_at_last(21)
cdll_obj.insert_at_last(35)
cdll_obj.insert_at_last(350)
cdll_obj.insert_item(cdll_obj.search(21), 89)
# cdll_obj.delete_first()
# cdll_obj.delete_last()
cdll_obj.delete_item(350)
cdll_obj.print_list()
for items in cdll_obj:
    # print(items, end=' ')
    pass