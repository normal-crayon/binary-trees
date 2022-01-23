

from binary_tree import Node
from tests import test
'''
depth first go depth wise, uses a stack to traverse the tree using a pointer and pushes the next node visited.
Remember: left node is more priority than right
Depth algo time complexity:  O(N)
''     ''  space complexity: O(N)

'''
@test
def depthFirstValues(root):
    if root == None:
        return []
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        #print(current.val + " ")

        if(current.left):
            stack.append(current.left)
        if(current.right):
            stack.append(current.right)
    return result


def depthFirstValues_Recursive(root):
    if root == None:
        return []
    lefts = depthFirstValues_Recursive(root.left)
    rights = depthFirstValues_Recursive(root.right)
    return [root.val] + rights + lefts


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')


a.left = b
a.right = d
b.right = c

depthFirstValues()

depthFirstValues_Recursive(a)
