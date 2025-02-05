#  ===== Assignment-14 Deque Implimentation Using List =====
# Note - Variations of Queue
# 1 - Insertion restricted
# In this case we insert value only rear side but delete both of the side front and rear
# 2 - Deletion restricted
# In this case we can insert value both of the side front and rear but delete front side

# 1. Define a class Deque to implement queue data structure using List. Define __init__() method to create an empty list object as instanse object member of Deque.
class Deque:
    def __init__(self):
        self.my_list = []

# 2. Define a method is_empty() to check if the deque is empty in Deque class.
    def is_empty(self):
        return self.my_list == None

# 3. In Deque class, define insert_front method to add data at the front end of the deque.
    def insert_front(self, data):
        if not self.is_empty():
            self.my_list.insert(0, data)
            # self.my_list[-1] = data

# 4. In Deque class, define insert_rear method to add data at the rear end of the deque.
    def insert_rear(self, data):
        # self.my_list[0] = data
        self.my_list.append(data)

# 5. In Deque class, define delete_front() method to remove front element from the deque.
    def delete_front(self):
        if not self.is_empty():
            self.my_list.pop(0)

# 6. In Deque class, define delete_rear() method to remove rear element from the deque.
    def delete_rear(self):
        if not self.is_empty():
            self.my_list.pop()

# 7. In Deque class, define get_front() method to return front element of the deque.
    def get_front(self):
        if not self.is_empty():
            print(self.my_list[0])

# 8. In Deque class, define get_rear() method to return rear element of the deque.
    def get_rear(self):
        if not self.is_empty():
            print(self.my_list[-1])

# 9. In Deque class, define size() method to return size of the deque that is number of items present in the deque.
    def size(self):
        return len(self.my_list)

deObj = Deque()
deObj.insert_front(21)
deObj.insert_rear(201)
deObj.insert_front(34)
deObj.get_front()
deObj.get_rear()
deObj.delete_rear()
print(deObj.size())