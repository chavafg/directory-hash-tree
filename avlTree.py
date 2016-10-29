# -*- coding: utf-8 -*-
from avlNode import avlnode
from item import DirectoryItem


class avltree(object):

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, key, DirectoryItem):
        # Create new node
        n = avlnode(key, DirectoryItem)

        # Initial tree
        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        # Insert key to the left subtree
        elif key < self.node.key:
            self.node.left.insert(key, DirectoryItem)
        # Insert key to the right subtree
        elif key > self.node.key:
            self.node.right.insert(key, DirectoryItem)

        # Rebalance tree if needed
        self.rebalance()

    def rebalance(self):
        # Check if we need to rebalance the tree
        #   update height
        #   balance tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # For each node checked,
        # if the balance factor remains −1, 0, or +1 then no rotations are
        # necessary.
        while self.balance < -1 or self.balance > 1:
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()

            # Right subtree is larger than left subtree
            if self.balance < -1:

                # Right Left Case -> rotate x,z to the right
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1 + max(self.node.left.height,
                                  self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key):
        if self.node != None:
            if self.node.key == key:
                print self.node.DirectoryItem
                # Key found in leaf node, just erase it
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                # Node has only one subtree (right), replace root with that one
                elif not self.node.left.node:
                    self.node = self.node.right.node
                # Node has only one subtree (left), replace root with that one
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # Find  successor as smallest node in right subtree or
                    #       predecessor as largest node in left subtree
                    # This is the case where the node is in the middle of the
                    # tree or is the root of the tree.
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.key = successor.key

                        # Delete successor from the replaced node right subree
                        self.node.right.delete(successor.key)

            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)

            # Rebalance tree
            self.rebalance()

    def search(self, key):
        if self.node != None:
            if self.node.key == key:
                print 'Found key ' + str(key)
                return self.node.DirectoryItem
            elif key < self.node.key:
                self.node.left.search(key)

            elif key > self.node.key:
                self.node.right.search(key)
        else:
            print 'Key ' + str(key) + ' was not found'

    def inorder_traverse(self):
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.DirectoryItem)
        result.extend(self.node.right.inorder_traverse())

        return result

    def display(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.display(node.right.node, level + 1)
            print ('\t' * level), ('    /')

        print ('\t' * level), node

        if node.left.node:
            print ('\t' * level), ('    \\')
            self.display(node.left.node, level + 1)

    def __str__(self):
        return str(self.node)

# Demo
if __name__ == "__main__":
    tree = avltree()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    record = DirectoryItem('TestUser', 'Test', 'address', 9990, 9999)

    #from random import randrange
    for key in data:
        tree.insert(key, record)

    for key in [4, 3]:
        tree.search(key)

    # for key in [12,58,35,4,98,45,33,25,19,56,67,81,99,32,49,77,101]:
    #    tree.insert(key)

    # print tree.inorder_traverse()
    print (tree.inorder_traverse())
    # tree.display()
    print (tree)
