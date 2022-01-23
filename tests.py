from binary_tree import Node

def test(func):
    def testing(*args, **kwargs):
        '''
        The test binary tree is \n
                a
                /\
               b  c
              /  / \ 
             d  e   f
        '''
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')

        a.left = b
        a.right = c
        b.left = d
        c.left = e
        c.right = f

        results = func(a, *args)

        print("result are: ", results)

        return results
    return testing


def num_test(func):
    def num_testing(*args, **kwargs):
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

        results = func(a)
        print("results: ", results)
        return results

    return num_testing 

