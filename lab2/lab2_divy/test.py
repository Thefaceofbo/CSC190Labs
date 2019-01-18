from binary_tree import *
from tree import *

def test1():
    x = tree(1000)
    y = tree(2000)
    z = tree(3000)
    c = tree(5000)
    d = tree(6000)
    e = tree(7000)
    f = tree(8000)
    g = tree(9000)
    x.AddSuccessor(y)
    x.AddSuccessor(z)
    y.AddSuccessor(c)
    y.AddSuccessor(d)
    z.AddSuccessor(e)
    z.AddSuccessor(f)
    z.AddSuccessor(g)
    x.Print_DepthFirst()
    print(x.Get_LevelOrder())
    return True

def test2():
    a = binary_tree(1000)
    b = binary_tree(2000)
    c = binary_tree(3000)
    d = binary_tree(4000)
    e = binary_tree(5000)
    f = binary_tree(6000)
    g = binary_tree(7000)
    a.AddLeft(b)
    a.AddRight(c)
    b.AddLeft(d)
    b.AddRight(e)
    c.AddLeft(f)
    c.AddRight(g)
    print(a.Get_LevelOrder())
    return True


def test3():
    a = binary_tree(1000)
    b = binary_tree(2000)
    a.AddRight(b)
    print(a.store)
    return True

test3()