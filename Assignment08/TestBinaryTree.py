

#  File: TestBinaryTree.py

#  Description: Functions for the Binary Tree

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name: Eric Deng

#  Partner UT EID: ed36549

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 3/22/2022

#  Date Last Modified: 3/22/2022


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root == None:
            return 'undefined'
        if self.root.lChild == self.root.rChild == None:
            return 0
        curr = self.root
        while curr.rChild != None:
            curr = curr.rChild
        maximum = curr.data
        curr = self.root
        while curr.lChild != None:
            curr = curr.lChild
        minimum = curr.data

        return maximum - minimum


    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        if self.root == None:
            return []
        level_lst = [self.root]
        for i in range(level):
            new_lst = []
            for n in level_lst:
                new_lst.append(n.lChild)
                new_lst.append(n.rChild)
            level_lst = new_lst
            while None in level_lst:
                level_lst.remove(None)
        return level_lst


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        if self.root == None:
            return []
        return []

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        children_lst = [self.root]
        while True:
            new_lst = []
            for n in children_lst:
                if n == None:
                    pass
                elif type(n) != Node:
                    new_lst.append(n)
                elif n.lChild == None == n.rChild:
                    new_lst.append(n.data)
                elif n.lChild == None:
                    new_lst.append(n.rChild)
                elif n.rChild == None:
                    new_lst.append(n.lChild)
                else:
                    new_lst.append(n.lChild)
                    new_lst.append(n.rChild)
            children_lst = new_lst
            if all(isinstance(x, int) for x in children_lst):
                break
        return sum(children_lst)






def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()



