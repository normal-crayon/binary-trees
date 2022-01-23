from binary_tree import Node
from tests import test

@test
def breadthFirstValues(root):
    if root == None:
        return []
    values = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        values.append(current.val)

        if current.left != None:
            queue.append(current.left)

        if current.right != None:
            queue.append(current.right)

    return values


breadthFirstValues()