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

    # notes on algorithm approaches
    # 1. how to get middle value of linked list (halfway between beginning and end)
    # use two vars. for each step send first two node ahead, send second one node ahead
    # when first node is at end, second node will be halfway through list
    # 2. how to reverse singly linked list
    # create previous, current, and next variables
    # reverse next pointer on the different nodes

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head:
            previous_head = self.head
            self.head = ListNode(value, prev=None, next=previous_head)
            previous_head.prev = self.head
            self.length += 1
        else:
            # case where there is no head
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return None
        if self.head.next:
            removed_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return removed_head.value
        else:
            # case where there is only one node, the head
            removed_head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail and self.tail is not self.head:
            # case with multiple nodes in doubly linked list
            prev_tail = self.tail
            self.tail = ListNode(value, prev=prev_tail)
            prev_tail.next = self.tail
            self.length += 1
        elif self.tail is not None and self.tail is self.head:
            # case with 1 node, head and tail are same
            self.tail = ListNode(value)
            self.tail.prev = self.head
            self.head.next = self.tail
            self.length += 1
        else:
            # case with no head or tail
            self.tail = ListNode(value)
            self.head = self.tail
            self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        elif self.tail.prev is None:
            prev_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return prev_tail.value
        prev_tail = self.tail
        self.tail = prev_tail.prev
        self.tail.next = None
        self.length -= 1
        return prev_tail.value
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""   
    def move_to_front(self, node):
        if self.head is node:
            return None
        elif self.tail is node:
            # remove node from list
            self.tail = node.prev
            node.prev.next = None
            # add node at head
            prev_head = self.head
            self.head = node
            self.head.prev = None
            self.head.next = prev_head
            prev_head.prev = self.head
        else:
            # remove node from list
            node.prev.next = node.next
            node.next.prev = node.prev
            # add node at head
            prev_head = self.head
            self.head = node
            self.head.prev = None
            self.head.next = prev_head
            prev_head.prev = self.head


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail is node:
            return None
        elif self.head is node:
            # remove node from list
            self.head = node.next
            self.head.prev = None
            # add node to tail
            prev_tail = self.tail
            self.tail = node
            self.tail.prev = prev_tail
            self.tail.next = None
            prev_tail.next = self.tail
        else:
            # remove node from list
            node.prev.next = node.next
            node.next.prev = node.prev
            # add node to tail
            prev_tail = self.tail
            self.tail = node
            self.tail.prev = prev_tail
            self.tail.next = None
            prev_tail.next = self.tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        iter_node = self.head
        max_value = iter_node.value
        while iter_node.next:
            iter_node = iter_node.next
            if iter_node.value > max_value:
                max_value = iter_node.value
        return max_value
        