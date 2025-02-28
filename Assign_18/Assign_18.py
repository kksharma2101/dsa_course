#  ===== Assignment-20 Binary Search Tree Part-1 =====

# Note - A tree is defined as a finite set of one or more data items (nodes), Such that There is special node called the root node of the tree and the remaining nodes are partitioned into n >= 0 disjoint subsets, each of which is itself a tree, and they are known as subtrees.
# A tree data structure is a hierarchical, non-linear data structure that resembles a tree with a root, branches, and leaves. Unlike linear structures like arrays or linked lists, trees organize data in a parent-child relationship.

# => A tree with degree 2 its is called Binary Tree

# 1. Define a class Node with instance variables left, item and right. The variables left and right are used to refer left and right child node. The item variable is used to hold data item.
class Node:
    def __init__(self, item):
        self.left = None
        self.item = item
        self.right = None

# 2. Define a class BST to implement Binary Search Tree data structure. Make __init__() method to create root instance variable to hold the reference of root node.
class BST:
    def __init__(self, root=None):
        self.root = root

# 3. In class BST, define insert method to store new data item in the binary search tree.
    def insert(self, data):
        self.root = self.reinsert(self.root, data)

    def reinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.reinsert(root.left, data)
        else:
            root.right = self.reinsert(root.right, data)
        return root

        # n = Node(data)
        # if self.root is None:
        #     return n
        # current = self.root
        # while True:
            # if data < self.root.item:
            #     if current.left is None:
            #         current.left = n
            #         return
            #     current = current.left
            # elif data > self.root.item:
            #     if current.right is None:
            #         current.right = n
            #         return
            #     current = current.right



# 4. In class BST, Define a search method to find a given item in the binary search tree and returns the node reference. It returns None if search failed.
    def search(self, data):
        return self.research(self.root, data)
    
    def research(self, root, data):
        if root is None or root.item is data:
            return root
        if data < root.item:
            return self.research(root.left, data)
        else:
            return self.research(root.right, data)
        
        
# 5. In class BST, define a method to implement inorder traversal.
    def inorder(self, root, result=[]):
        if root:
            self.inorder(root.left, result )
            result.append(root.item)
            # print(root.item, end=" ")
            self.inorder(root.right,result )
        return result

# 6. In class BST, define a method to implement preorder traversal.
    def preorder(self, root, res=[]):
        if root:
            res.append(root.item)
            self.preorder(root.left, res)
            self.preorder(root.right, res)
        return res

# 7. In class BST, define a method to implement postorder traversal.
    def postorder(self, root, res=[]):
        if root:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.item)
        return res

bst = BST()
# bst.insert(51)
values = [45,32,78,21,23,67,89,90]
for value in values:
    bst.insert(value)

print(bst.inorder(bst.root))
print(bst.preorder(bst.root))
print(bst.postorder(bst.root))
# print(bst.search(45))