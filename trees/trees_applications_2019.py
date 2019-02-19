# -*- coding: utf-8 -*-
"""
Feb. 2019
S3#-api - trees part 3
"""

from algopy import tree
from algopy import treeasbin


"""
tree -> dot
"""

from  algopy import queue

def dot(T):
    """Write down dot format of tree.

    Args:
        ref (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    s += "node [shape=circle, fixedsize=true, height=0.5, width=0.5]\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s = s + "   " + str(T.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    s += "}"
    return s
  

'''
tree -> list representation
'''

def tree2list(T):
    s = '(' + str(T.key)
    for child in T.children:
        s += tree2list(child)
    s += ')'
    return s

def treeAsBin2list(B):
    s = '(' + str(B.key)
    C = B.child
    while C != None:
        s += treeAsBin2list(C)
        C = C.sibling
    s += ')'
    return s
    
    
def treeAsBin2list2(B):
    s = '(' + str(B.key)
    if B.child:
        s += treeAsBin2list2(B.child)
    s += ')'
    if B.sibling:
        s += treeAsBin2list2(B.sibling)
    return s


'''
Levels
list of levels: one list per level
from C3 2018
'''

def levels(T):
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    List = []
    level = []
    while not q.isempty():
        T = q.dequeue()
        if T == None:
            List.append(level)
            level = []
            if not q.isempty():
                q.enqueue(None)
        else:
            level.append(T.key)
            for child in T.children:
                q.enqueue(child)
    return List



'''
Average Arity: 
sum of the number of children per node divided by the number of internal nodes
from C3# 2018
'''
    
# with TreeAsBin
def __countnodestab(B):
    if B.child == None:
        return (0, 0)
    else:
        Bchild = B.child
        internnodes, nbchildren = 1, 0
        while Bchild != None:
            (nbi, nbc) = __countnodestab(Bchild)
            internnodes += nbi
            nbchildren += nbc + 1
            Bchild = Bchild.sibling
        return internnodes, nbchildren

def arityTAB(B):
    (nbi, nbc) = __countnodestab(B)
    return (nbc/nbi if nbi != 0 else 0)

#using the binary structure...
def __arity2(B):
    ''' 
    return (nb links, nb internal nodes)
    '''
    if B.child == None:
        (links, nodes) = (0, 0)
    else:
        (l, n) = __arity2(B.child)
        (links, nodes) = (l + 1, n + 1)
        
    if B.sibling != None:
        (l, n) = __arity2(B.sibling)
        links += l + 1
        nodes += n

    return (links, nodes)

def averagearity_bin2(B):
    (links, nodes) = __arity2(B)
    return 0 if nodes == 0 else links / nodes


'''
Equality of two trees (one of each implementation)
from C3 2018
'''

def equal(T, B):
    if T.key != B.key:
        return False
    else:
        i = 0
        C = B.child
        while i < T.nbchildren and C and equal(T.children[i], C):
            i += 1
            C = C.sibling
        return i == T.nbchildren and C == Non



"""
TreeAsBin -> Tree
"""

def treeasbin2tree(B):
    T = tree.Tree(B.key, [])
    child = B.child
    while child != None:
        T.children.append(treeasbin2tree(child))
        child = child.sibling
    return T

    
"""
Tree -> TreeAsBin
"""

def treeToTreeAsBin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    if T.nbchildren != 0:
        B.child = treeToTreeAsBin(T.children[0])
        S = B.child
        for i in range(1, T.nbchildren):    
            S.sibling = treeToTreeAsBin(T.children[i])
            S = S.sibling
    return B


def tree2TreeAsBin2(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    firstchild = None
    for i in range(T.nbchildren-1, -1, -1):
        C = tree2TreeAsBin2(T.children[i])
        C.sibling = firstchild
        firstchild = C
    
    B.child = firstchild
    return B



"""
list -> tree (int keys)
"""

def __list2tree(s, i=0): 
        i = i + 1 # to skip the '('
#        construire la clé = key
        key = ""
        while s[i] not in "()":
            key += s[i]
            i += 1
        T = tree.Tree(int(key), [])
#        construire T.children : appels récursifs
        while s[i] != ')':    # or s[i] == '('
            (C, i) = __list2tree(s, i)
            T.children.append(C)
        
        i += 1  # to skip ')'
        return (T, i)

def list2tree(L):
    (T, _) = __list2tree(L)
    return T




"""
BONUS : using binary structure of first child - right sibling implementation
"""

# TreeAsBin -> Tree
    
def __treeasbin2tree2(B, parent):
    '''
    convert B -> added as new child of parent
    '''
    newChild = tree.Tree(B.key)
    parent.children.append(newChild)
    if B.sibling:
        __treeasbin2tree2(B.sibling, parent)
    if B.child:
        __treeasbin2tree2(B.child, newChild)

def treeasbin2tree2(B):
    T = tree.Tree(B.key)
    if B.child:
        __treeasbin2tree2(B.child, T)
    return T


# Tree -> TreeAsBin

def __tree2tab(parent, i):
    '''
    build child #i of parent
    '''
    if i == parent.nbchildren:
        return None
    else:
        child_i = treeasbin.TreeAsBin(parent.children[i].key)
        child_i.sibling = __tree2tab(parent, i+1)
        child_i.child = __tree2tab(parent.children[i], 0)
        return child_i
    
def treeToTAB(T):
    return treeasbin.TreeAsBin(T.key, __tree2tab(T, 0), None)

# TreeAsBin -> linear represntation


def __list2treeasbin(s, i=0): 
    if i < len(s) and s[i] == '(':   
        i = i + 1 # to pass the '('
        key = ""
        while not (s[i] in "()"):
            key = key + s[i]
            i += 1
        B = treeasbin.TreeAsBin(int(key))
        (B.child, i) = __list2treeasbin(s, i)
        i = i + 1   # to pass the ')'
        (B.sibling, i) = __list2treeasbin(s, i)
        return (B, i)
    else:
        return (None, i)

def list2treeasbin(s):
    return __list2treeasbin(s)[0]


"(15(3(-6)(10))(8(11(0)(4))(2)(5))(9))"



        
