from binary_tree import Node
from tests import num_test

@num_test
def depthFirstIter(root):
    '''
    Iterative depth first approach using stack
    '''
    smallest = float('inf')
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val
        
        if current.left != None:
            stack.append(current.left)
        
        if current.right != None:
            stack.append(current.right)
        
    return smallest

@num_test
def bredthFirstIter(root):
    '''
    Iterative bredth first approach using queue
    '''
    smallest = float('inf')
    stack = [root]
    while len(stack) > 0:
        current = stack.pop(0)
        if current.val < smallest:
            smallest = current.val
        
        if current.left != None:
            stack.append(current.left)
        
        if current.right != None:
            stack.append(current.right)
        
    return smallest

def depthFirstRecur(root):
    if root == None:
        return float('inf')

    leftMin = depthFirstIter(root.left)
    rightMin = depthFirstIter(root.right)

    return min(root.val, leftMin, rightMin)



depthFirstIter()
bredthFirstIter()