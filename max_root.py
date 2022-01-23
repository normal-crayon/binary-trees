from binary_tree import Node

def max_path(root):
    '''
    recursive path finding method to find the max path of num binary tree
    '''
    if root == None:
        return float('-inf')
    
    if root.left == None and root.right == None:
        return root.val
    
    maxPath = max(max_path(root.left), max_path(root.right))
    return root.val + maxPath


a = Node(11)
b = Node(25)
c = Node(3)
d = Node(13)
e = Node(45)
f = Node(10)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f 

print("result: ", max_path(a))