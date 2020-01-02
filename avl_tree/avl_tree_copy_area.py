
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

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

    def update_balance(self):
        left_height = 0
        right_height = 0

        if self.node.left:
            left_height = self.node.left.update_height() + 1
        if self.node.right:
            right_height = self.node.right.update_height() + 1

        self.balance = left_height - right_height


    def left_rotate(self):
        new_left_tree = self
        new_parent_tree = self.node.right
        self = new_parent_tree
        self.node.left = new_left_tree
        self.node.left.node.right = None
        print("#2 Displaying correctly rotated tree within right_rotate(self)")
        self.display()
    
    def right_rotate(self):
        new_right_tree = self
        new_parent_tree = self.node.left
        self = new_parent_tree
        self.node.right = new_right_tree
        self.node.right.node.left = None
        print("#2 Displaying correctly rotated tree within right_rotate(self)")
        self.display()

        return self

    def rebalance(self):
        # TODO filter for left rotation, left right rotation, right left rotation

        if self.balance == -2:
            self.display()
            self.left_rotate()
            self.display()

        if self.balance == 2:
            print("#1 Displaying tree before right rotation")
            self.display()
            self.right_rotate()
            print("#3 Displaying buggy tree after right rotation, outside of function")
            self.display()

    def insert(self, key):
        if self.node == None:
            self.node = Node(key)
            return

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
        if self.balance > 1 or self.balance < -1:
            self.rebalance()

# running code

test_tree = AVLTree(Node(2))
test_tree.insert(3)
test_tree.insert(5)