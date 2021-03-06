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
        self.update_height()
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[height {self.height}: balance {self.balance}]',
                   'Leaf' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

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
            left_height = self.node.left.update_height() + 1
        if self.node.right:
            right_height = self.node.right.update_height() + 1
        
        # print("left height", left_height, "right height", right_height)
        self.balance = left_height - right_height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        new_left_tree = self
        new_parent_tree = self.node.right
        self = new_parent_tree
        self.node.left = new_left_tree
        self.node.left.node.right = None
        print("#2 Displaying correctly rotated tree within right_rotate(self)")
        self.display()

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        # this only works with 2 left nodes (i.e. inserting 5, 3, then 2 into a binary search tree)
        print("before right rotate")
        print("current self", self.node.key)

        # the new right node will be the current parent node
        new_right_tree = self
        # print(new_right_tree.node.key)
        
        # the new parent node will be the left node of the current parent node
        new_parent_tree = self.node.left
        # print(new_parent_tree.node.key)

        # assign new parent tree
        self = new_parent_tree
        # print(self.node.key)

        # assigns old parent to new right tree
        self.node.right = new_right_tree

        # remove old left side from old parent
        self.node.right.node.left = None

        print("new self at end of right rotation function", self.node.key)
        self.display()

        return self


    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """

    def rebalance(self):
        if self.balance == -2:
            self.left_rotate()
        
        if self.balance == 2:
            print("rebalancing print statements")
            print("before rotation key", self.node.key)
            self.right_rotate()
            print("after rotation key", self.node.key)
            print("rebalancing print statements")
        
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
            print("out of balance", self.balance, self.node.key)
            self.rebalance()

test_tree = AVLTree(Node(2))
test_tree.display()
test_tree.insert(3)
test_tree.display()
# print(test_tree.node.left.node.key)
print("before last insert")
test_tree.insert(5)
print("after last insert")
test_tree.display()
# print(test_tree.node.left.node.key)
# print(test_tree.node.left.node.left.node.key)
# print(test_tree.height)
# test_tree.update_balance()
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