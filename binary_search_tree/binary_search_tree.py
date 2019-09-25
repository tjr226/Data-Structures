import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

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
        print_queue = Queue()
        print_queue.enqueue(node)

        # return_string = ""

        while print_queue.len() > 0:
            current_node = print_queue.dequeue()
            # if current_node:
            #     return_string += f"{current_node.value}\n"
            print(current_node.value)
            if current_node.left:
                print_queue.enqueue(current_node.left)
            if current_node.right:
                print_queue.enqueue(current_node.right)
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print_stack = Stack()
        print_stack.push(node)

        while print_stack.len() > 0:
            current_node = print_stack.pop()
            print(current_node.value)
            if current_node.left:
                print_stack.push(current_node.left)
            if current_node.right:
                print_stack.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print_stack = Stack()
        print_stack.push(node)

        while print_stack.len() > 0:
            current_node = print_stack.pop()
            print(current_node.value)
            if current_node.right:
                print_stack.push(current_node.right)
            if current_node.left:
                print_stack.push(current_node.left)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        order_stack = Stack()
        order_stack.push(node)
        print_stack = Stack()

        while order_stack.len() > 0:
            current_node = order_stack.pop()
            print_stack.push(current_node)
            if current_node.left:
                order_stack.push(current_node.left)
            if current_node.right:
                order_stack.push(current_node.right)

        while print_stack.len() > 0:
            print(print_stack.pop().value)



# test_bst = BinarySearchTree(1)
# test_bst.insert(8)
# test_bst.insert(5)
# test_bst.insert(7)
# test_bst.insert(6)
# test_bst.insert(3)
# test_bst.insert(4)
# test_bst.insert(2)

# test_bst.in_order_print(test_bst)

# test_bst.bft_print(test_bst)