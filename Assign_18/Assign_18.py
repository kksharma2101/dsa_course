#  ===== Assignment-20 Binary Search Tree Part-1 =====

# Note - A tree is defined as a finite set of one or more data items (nodes), Such that There is special node called the root node of the tree and the remaining nodes are partitioned into n >= 0 disjoint subsets, each of which is itself a tree, and they are known as subtrees.
# A tree data structure is a hierarchical, non-linear data structure that resembles a tree with a root, branches, and leaves. Unlike linear structures like arrays or linked lists, trees organize data in a parent-child relationship.

# => A tree with degree 2 its is called Binary Tree

# 1. Define a class Node with instance variables left, item and right. The variables left and right are used to refer left and right child node. The item variable is used to hold data item.
class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right

# 2. Define a class BST to implement Binary Search Tree data structure. Make __init__() method to create root instance variable to hold the reference of root node.
class BST:
    def __init__(self, root=None):
        self.root = root

# 3. In class BST, define insert method to store new data item in the binary search tree.
    def insert(self, data):
        n = Node(data)
        if self.root is None:
            self.root = n
        elif self.root.item.left is None and self.root.item.right is None:
            if self.root.item > data:
                self.root.left = n
            else:
                self.root.right = n
        else:
            temp = self.root
            if self.root.item > data:
                while temp.item > data:
                    temp



# 4. In class BST, Define a search method to find a given item in the binary search tree and returns the node reference. It returns None if search failed.

# 5. In class BST, define a method to implement inorder traversal.

# 6. In class BST, define a method to implement preorder traversal.

# 7. In class BST, define a method to implement postorder traversal.