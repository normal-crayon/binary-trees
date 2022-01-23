from binary_tree import Node
from tests import num_test, test

def depthFirstSum(root):
    if root == None:
        return 0
    
    return root.val + depthFirstSum(root.left) + depthFirstSum(root.right)

@num_test
def bredthFirstSum(root):
    if root == None:
        return 0
    
    sum = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        sum += current.val

        if current.left != None:
            queue.append(current.left)
        
        if current.right != None:
            queue.append(current.right)

    return sum


bredthFirstSum()