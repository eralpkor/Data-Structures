"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # 1. create a new node with the value it's given
        new_node = ListNode(value)
        # add to the length of linked list
        self.length += 1
        # if no head node and no tail node set it to new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # there are nodes in linked list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # 1. create a new node with the value it's given
        new_node = ListNode(value)
        # 2 add to the length +1
        self.length += 1
        # if the list is initially empty, set both head and tail to the new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # setup prev link to new node
            new_node.prev = self.tail
            # make the link from self to new node
            self.tail.next = new_node
            # link to tail as reference to the last node.
            self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # assign value to be deleted 
        value = self.tail.value
        # remove the node from tail
        self.delete(self.tail)
        # return the deleted node
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -=1
        # call the class ListNode delete
        # remove the references
        node.delete()
        # replace the pointers
        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        max_val = self.head.value
        while current_node:
            max_val = current_node.value if current_node.value\
                 > max_val else max_val
            current_node = current_node.next
        return max_val

    # This function prints contents of linked list 
    # starting from the given node 
    def printList(self, node):
        print('\nTraversal in forward direction')
        while (node is not None):
            print('% d' %(node.value))
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last is not None:
            print(' % d' %(last.value))
            last = last.prev

# llist = DoublyLinkedList()            
# llist.add_to_head(6)
# llist.printList(llist.head)