from binary_tree import Node
from tests import rec_test, test
from tree_sum import depthFirstSum

@test
def breadthFirstSearch(root, target):
    if root == None:
        return False
    
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)

        if(current.val == target):
            return True
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return False

def depthFirstSearch(root, target):
    if root == None:
         return False
    
    if root.val == target:
        return True
    
    return depthFirstSearch(root.left, target) or depthFirstSearch(root.right, target)

breadthFirstSearch('e')

