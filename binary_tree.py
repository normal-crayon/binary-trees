class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')


a.left = b
a.right = d
b.right = c


#       a
#      / \
#     b   d
#    /
#   c


