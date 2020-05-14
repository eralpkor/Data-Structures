from collections import deque
from dll_stack import Stack
from dll_queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
0. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
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

    # iterative for each depth first
    def iterative_for_each(self, fn):
        stack = []
        # add the root node
        stack.append(self)

        #loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)

    # breadth first for each
    def breadth_first_for_each(self, fn):
        queue = deque()
        # add the root node
        queue.append(self)

        #loop so long as the stack still has elements
        while len(queue) > 0:
            current = queue.pop()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
# traversals require O(n) time as they visit every node exactly once.
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # print current node first then
        # print to the right (largest node) until none
        # go to left node (subtree) print first node
        # print right subtree leafs left node
        to_print = Queue()
        to_print.enqueue(node)
        current_node = to_print.dequeue()
        while current_node: # is not None
            # print current node 
            print(current_node.value)
            # if there is right node of current node, 
            if current_node.right:
                # call Queue.enqueue until no right leaf (node)
                to_print.enqueue(current_node.right)
            # if there is left node of current node

            if current_node.left:
                to_print.enqueue(current_node.left)
            if to_print.size > 0:
                current_node = to_print.dequeue()
            else:
                # quit when Queue size is 0
                break

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Go left (small values) first then right (small leafs)
    def dft_print(self, node):
        to_print = Stack() # using stack
        to_print.push(node) # add first node to the stack
        # while stack length greater then 0
        while to_print.__len__() > 0:
            # pop the node from stack assign to var current
            current = to_print.pop()
            # print the current node value
            print(current.value)
            # if right node value exist 
            if current.right:
                # add to tail
                to_print.push(current.right)
            if current.left:
                to_print.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


root = BinarySearchTree(40)
root.insert(80)
root.insert(50)
root.insert(70)
root.insert(60)
root.insert(30)
root.insert(35)
root.insert(25)
root.insert(20)
root.insert(10)
root.insert(90)


# root.in_order_print(root)
print('$$$$$$$$$$ Nothing to see here $$$$$$$$$$$$$$$$')
root.bft_print(root)
# root.dft_print(root)

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

# Notes on recursion and when you need a return:
# you need a return when the function calls will be passing a value to up to the original function call (e.g. you need a concrete answer in the end).
# the return is what allows the value in question to leave its scope and enter the previous call's scope.
# for_each doesn't have a return (web students remember map returns a new copy but forEach doesn't return anything)
# because there is no need to pass data along to the original function call, there is no need for a return