#  File: ExpressionTree.py

#  Description: Expression Tree evaluation and prefix, postfix forms

#  Student Name: Austin Yeh

#  Student UT EID: ay6922

#  Partner Name: Eric Deng

#  Partner UT EID: ed36549

#  Course Name: CS 313E

#  Unique Number: 51135

#  Date Created: 3/17/2022

#  Date Last Modified: 3/17/2022

from pdb import post_mortem
import sys

operators = ["+", "-", "*", "/", "//", "%", "**"]


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self) -> str:
        return self.stack.__str__()


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        lst = expr.split(" ")
        stack = Stack()
        self.root = Node()
        current_node = self.root
        for token in lst:
            if token == "(":
                current_node.lChild = Node()
                stack.push(current_node)
                current_node = current_node.lChild
            elif token in operators:
                current_node.data = token
                stack.push(current_node)
                current_node.rChild = Node()
                current_node = current_node.rChild
            elif token == ")":
                current_node = stack.pop()
            else:
                current_node.data = token
                current_node = stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode.data == "+":
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        elif aNode.data == "-":
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        elif aNode.data == "*":
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        elif aNode.data == "/":
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        elif aNode.data == "//":
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        elif aNode.data == "%":
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        elif aNode.data == "**":
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        else:
            return float(aNode.data)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if aNode.lChild is None and aNode.rChild is None:
            return aNode.data
        elif aNode.lChild is None:
            return self.pre_order(aNode.rChild)
        elif aNode.rChild is None:
            return self.pre_order(aNode.lChild)
        else:
            return (
                aNode.data
                + " "
                + self.pre_order(aNode.lChild)
                + " "
                + self.pre_order(aNode.rChild)
            )

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if aNode.lChild is None and aNode.rChild is None:
            return aNode.data
        elif aNode.lChild is None:
            return self.post_order(aNode.rChild)
        elif aNode.rChild is None:
            return self.post_order(aNode.lChild)
        else:
            return (
                self.post_order(aNode.lChild)
                + " "
                + self.post_order(aNode.rChild)
                + " "
                + aNode.data
            )


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
