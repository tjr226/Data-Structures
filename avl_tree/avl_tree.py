import math
"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'Leaf' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    # def display_no_update(self, level=0, pref=''):
    #     # self.update_height()  # Update height before balancing
    #     # self.update_balance()

    #     if self.node != None: 
    #         print ('-' * level * 2, pref, self.node.key,
    #                 f'[{self.height}:{self.balance}]',
    #                 'Leaf' if self.height == 0 else ' ')
    #         if self.node.left != None:
    #             self.node.left.display_no_update(level + 1, '<')
    #         if self.node.right != None:
    #             self.node.right.display_no_update(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """

    def update_height(self):
        max_height = 0

        if self.node.left or self.node.right:
            left_height = 0
            right_height = 0
            if self.node.left:
                left_height = self.node.left.update_height() + 1
            if self.node.right:
                right_height = self.node.right.update_height() + 1
            max_height = max(left_height, right_height)

        self.height = max_height
        return max_height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        left_height = 0
        right_height = 0

        if self.node.left:
            left_height = self.node.left.update_height()
        if self.node.right:
            right_height = self.node.right.update_height()

        self.balance = left_height - right_height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        # print("before left rotate")
        # self.display_no_update()
        # set up vars
        new_left_tree = self.node.right
        new_parent_tree = new_left_tree.node.right
        # assign new parent tree
        self.node.right = new_parent_tree
        # remove old right side from old parent
        
        new_left_tree.node.right = new_parent_tree.node.left
        # add to new parent
        self.node.right.node.left = new_left_tree

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        # print("before right rotate")
        # self.display_no_update()
        # set up vars
        new_right_tree = self.node.left
        new_parent_tree = new_right_tree.node.left

        # assign new parent tree
        self.node.left = new_parent_tree
        # remove old left side from old parent
        new_right_tree.node.left = new_parent_tree.node.right
        # add to new parent
        self.node.left.node.right = new_right_tree


    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        if self.balance == -2:
            self.left_rotate()
        
        if self.balance == 2:
            self.right_rotate()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if self.node == None:
            self.node = Node(key)
            return

        # print("key and self node are", key, self.node.key)
        if key < self.node.key:
            if self.node.left == None:
                self.node.left = AVLTree(Node(key))
            else:
                self.node.left.insert(key)
        elif key >= self.node.key:
            if self.node.right == None:
                self.node.right = AVLTree(Node(key))
            else:
                self.node.right.insert(key)

        self.update_balance()


        # print(f"self balance is {self.balance}")
        if self.balance > 1 or self.balance < -1:
            # print("out of balance", self.balance)
            self.rebalance()

test_tree = AVLTree(Node(5))
test_tree.display()
test_tree.insert(3)
test_tree.display()
# print(test_tree.node.left.node.key)
test_tree.insert(2)
test_tree.display()
print(test_tree.node.left.node.key)
print(test_tree.node.left.node.left.node.key)
# test_tree.insert(6)
# print(test_tree.node.right.node.key)
# test_tree.display()
# test_tree.insert(7)
# print(test_tree.node.right.node.right.node.key)
# test_tree.display()
# test_tree.insert(1)
# test_tree.insert(8)

# print("final display")
# test_tree.display()

# test_tree.node.left.display()
# print(test_tree.height)
# print(test_tree.node.right.height)