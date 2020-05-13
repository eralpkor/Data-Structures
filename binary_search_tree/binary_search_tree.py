"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BinarySearchTree class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BinarySearchTree class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if insert value is less then node value
        if value < self.value:
            # and if is not 
            if  not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        # check if value is target (if it is return true)
        if target == self.value:
            return True
        # check if target is greater then the Node value
        elif target > self.value:
            # go right if right is a BSTNode
            return self.right.contains(target) if self.right else False
        else:
            # go left if left is a BST
            return self.left.contains(target) if self.left else False
        

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.left and self.in_order_print(node.left)
        print(node.value)
        node.right and self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



bst = BinarySearchTree(20)
bst.left = BinarySearchTree(10)
bst.right = BinarySearchTree(34)
bst.left.left = BinarySearchTree(4)
bst.left.right = BinarySearchTree(50)
bst.right.left = BinarySearchTree(21)

print(bst.contains(20))
print(bst.contains(10))
print(bst.contains(34))

print(bst.contains(50))
print(bst.contains(21))
print(bst.contains(111))
