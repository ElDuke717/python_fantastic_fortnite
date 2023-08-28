# Class or constructor for the nodes of a BST in Python
class Node:
    def __init__(self, val):  # note the use of __init__, it's like "constructor" in JavaScript
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
