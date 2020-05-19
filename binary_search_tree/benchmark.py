import time
import random
from binary_search_tree import BinarySearchTree as BSTNode

bst = BSTNode(500)

for _ in range(100000):
    bst.insert(random.randint(1, 1000))

fn = lambda x: x

start_time = time.time()
bst.for_each(fn)
end_time = time.time()

print(f"Recursive for_each ran in {end_time - start_time} seconds")

start_time = time.time()
bst.iterative_for_each(fn)
end_time = time.time()

print(f"Iterative for_each ran in {end_time - start_time} seconds")