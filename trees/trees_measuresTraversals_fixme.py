# -*- coding: utf-8 -*-

from algopy import tree, treeasbin

from algopy import queue

"""
Measures
"""

def size(T):
    """
    T: Tree
    """
    s = 1
    for i in range(T.nbchildren):
        s += size(T.children[i])
    return s

def sizeasbin(B):
    """
    B: TreeAsBin
    """
    s = 1
    child = B.child
    while child != None :
        s += sizeasbin(child)
        child = child.sibling
    return s

def sizeasbin2(B):
    if B == None:
        return 0
    else:
        return 1 + sizeasbin2(B.child) + sizeasbin2(B.sibling)
                
# height

def height(T):
    h = 0
    for child in T.children:
        h = max(h, height(child)+1)
    return h

def heightasbin(B):
    h = -1
    C = B.child
    while C != None:
        h = max(h, heightasbin(C))
        C = C.sibling
    return h + 1

def heightasbin2(B):
    if B == None:
        return -1
    else:
        return max(1 + heightasbin2(B.child), heightasbin2(B.sibling))
    

    
# Average External Depth (Profondeur moyenne externe)

def __average_external_depth(T, depth=0):
    if T.nbchildren == 0:
        return (depth, 1)
    else:
        depthsum = 0
        nbl = 0
        for i in range(T.nbchildren):
            (s, n) = __average_external_depth(T.children[i], depth + 1)
            depthsum += s
            nbl += n
        return (depthsum, nbl)

def average_external_depth(T):
    (epl, nbl) = __average_external_depth(T)  
    return epl / nbl


def __average_external_depth_bin(B, depth=0):
    if B.child is None:
        return (depth, 1)
    else:
        depthsum = 0
        nbl = 0
        C = B.child
        while B.child:
            (s, n) = __average_external_depth(C, depth + 1)
            depthsum += s
            nbl += n
            C = C.sibling
        return (depthsum, nbl)

def average_external_depth_bin(B):
    """
    B: TreeAsBin
    """
    (epl, nbl) = __average_external_depth_bin(B)  
    return epl / nbl
           
def __average_external_depth_bin2(B, depth=0):
     if B.child:    # if B.child != None
         (depthsum, nbl) = __average_external_depth_bin2(B.child, depth + 1)
     else:
         (depthsum, nbl) = (depth, 1)
     if B.sibling:
        (s, n) = __average_external_depth_bin2(B.sibling, depth)
        depthsum += s
        nbl += n
     return (depthsum, nbl)

def average_external_depth_bin2(B):
    """
    B: TreeAsBin
    """
    (epl, nbl) = __average_external_depth_bin2(B)
    return epl / nbl

     
"""
Traversals
"""

"""
Depth First Search
"""

# simple DFS (without intermediate)

def dfs(T):
    print(T.key)    # preorder
    for child in T.children:
        dfs(child)
    # postorder

def dfsasbin(B):
    print(B.key)    # preorder
    C = B.child
    while C:
        dfs(C)
        C = C.sibling
    # postorder

# full dfs (with intermediate)        

def dfs_full(T):
    print(T.key)    # preorder
    if T.nbchildren != 0:
        for i in range(T.nbchildren - 1):
            dfs(T.children[i])
            # intermediate
        dfs(T.children[T.nbchildren-1])
    # postorder
        
def dfsasbin_full(B):
    print(B.key) # preorder
    if B.child != None:
        child = B.child
        while child.sibling != None:
            dfsasbin(child)
            child = child.sibling
             # intermediate
        dfsasbin(child)
    # postorder

"""
Breadth First Search
"""


# first version: a "end level mark" (None) is added in the queue

def bfs(T):
    #FIXME
    pass

#second version: two queues

def bfsasbin(B):
    #FIXME
    pass
