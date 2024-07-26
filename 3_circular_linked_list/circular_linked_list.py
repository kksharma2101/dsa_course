# Assignment-5: Circular Linked List

# 1. Define a class Node to describe a node of a circular linked list.
class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

# 2. Define a class CLL to implement circular linked list with __init__() method to create and initialise last refference variable.
class CLL:
    def __init__(self, tail = None):
        self.tail = tail
    
# 3. Define a method is_empty() to check if the linked list is empty in CLL class.
    def is_empty(self):
        return self.tail == None
        
# 4. Define a method insert_at_start() to insert an element at the starting of the list
    def insert_at_start(self, data):
        n=Node(data)
        if self.is_empty():
            n.next = n
            self.tail = n
        else:
            n.next = self.tail.next
            self.tail.next = n
        
# 5. Define a method insert_at_last() to insert an element at the end of the list
    def insert_at_last(self, data):
        n=Node(data)
        if self.is_empty():
            n.next = n
            self.tail = n
        else:
            n.next = self.tail.next
            self.tail.next = n
            self.tail = n
     
# 6. Define a method search() to find the node with specified element value.
    def search(self, data):
        if self.is_empty():
            return None
        # elif self.tail.item == data:
        #     return self.tail
        # else:
        #     temp = self.tail.next
        #     while temp == self.tail.next:
        #         if temp.item == data:
        #             return temp
        #         temp = temp.next
        #         break
        #     return None
        # d
        temp = self.tail.next
        while temp != self.tail:
            if temp.item == data:
                return temp
            temp=temp.next
        if temp.item == data:
            return temp
        return None

# 7. Define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self,temp, data):
        if temp is not None:
            n=Node(data, temp.next)
            temp.next = n
            if temp == self.tail:
                self.tail = n
            
# 8. Define a method to print_all() the elements of the list.

    def print_all(self):
        if not self.is_empty():
            temp = self.tail.next
            while temp != self.tail:
                print(temp.item, end=" ")       
                temp = temp.next
            print(temp.item)

# 9. Define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if not self.is_empty():
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next

# 10. Define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if not self.is_empty():
            if self.tail.next == self.tail:
                self.tail = None
            else:
                temp=self.tail.next
                while temp.next != self.tail:
                    temp=temp.next
                temp.next = self.tail.next
                self.tail=temp

# 11. Define a method delete_item() to specified element from the list.
    def delete_item(self,data):
        if not self.is_empty():
            if self.tail.next == self.tail:
                if self.tail.item == data:
                    self.tail = None
            else:
                if self.tail.next.item == data:
                    self.delete_first()
                else:
                    temp = self.tail.next
                    while temp != self.tail:
                        if temp.next == self.tail:
                            if self.tail.item == data:
                                self.delete_last()
                            break
                        if temp.next.item == data:
                            temp.next == temp.next.next
                            break
                        temp=temp.next
                        
    def __iter__(self):
        if self.tail == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.tail.next)

# 12. Implement iterator for CLL to access all the elements of the list in a sequence.
class CLLIterator():
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        
        return data
    


obj = CLL()
obj.insert_at_start(21)
obj.insert_at_start(201)
obj.insert_at_start(301)
obj.insert_at_last(11)
obj.insert_at_last(2011)
obj.insert_after(obj.search(201),50)
# obj.delete_first()
# obj.delete_last()
obj.delete_item(11)
obj.print_all()
for temp in obj:
    print(temp, end=' ')
# 201, 21, 40, 2011