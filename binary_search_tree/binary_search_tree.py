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
        # if insert (incoming) value is less then current node value
        if value < self.value:
            # and if is not
            if not self.left:
                # set the value here
                self.left = BinarySearchTree(value)
            else:
                # keep searching
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
        current = self
        # Find the rightmost leaf node
        # As long as self.right exist keep going right;
        while current.right:
            # keep assigning right leaf to self (current)
            current = current.right
        # if no value left to the right return value
        return current.value

        # working while loop
        # while True:
        #     if current.right is not None:
        #         current = current.right
        #     elif current.right is None:
        #         return current.value

        # recursive solution
        # if self.right:
        #     return self.right.get_max()
        # return self.value

    def iterative_get_max(self):
        current_nax = self.value
        current = self
        # traverse our structure
        while current:
            if current.value > current_nax:
                current_nax = current.value
            # update our current max variable if we see a larger value
            current = current_nax
        return current_nax

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # at the leaf node
        fn(self.value)
        # if left leaf exist
        if self.left:
            # call recursive
            self.left.for_each(fn)
        # if right leaf
        if self.right:
            # call recursive
            self.right.for_each(fn)

    # iterative for each
    def iterative_for_each(self):
        stack = []

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

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


root = BinarySearchTree(1)
root.insert(8)
root.insert(5)
root.insert(7)
root.insert(6)
root.insert(3)
root.insert(4)
root.insert(2)

root.in_order_print(root)


# root = BinarySearchTree(20)
# root.left = BinarySearchTree(10)
# root.right = BinarySearchTree(34)
# print(root.in_order_print())
# bst.left.left = BinarySearchTree(4)
# bst.left.right = BinarySearchTree(50)
# bst.right.left = BinarySearchTree(21)

# print(bst.contains(20))
# print(bst.contains(10))
# print(bst.contains(34))

# print(bst.contains(50))
# print(bst.contains(21))
# print(bst.contains(111))
# print(bst.get_max())
