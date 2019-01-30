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
    #FIXME
    pass

def average_external_depth(T):
    (epl, nbl) = __average_external_depth(T)  
    return epl / nbl


def __average_external_depth_bin(B, depth=0):
    #FIXME
    pass

def average_external_depth_bin(B):
    """
    B: TreeAsBin
    """
    (epl, nbl) = __average_external_depth_bin(B)  
    return epl / nbl

# bonus: usig the binary structure?           
def __average_external_depth_bin2(B, depth=0):
    #FIXME
    pass


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
Depth First Search (DFS)
"""
 # write DFS: insert preorder, intermediates and postorder
 
def dfs(T):
    #FIXME
    pass
        
def dfsasbin(B):
     #FIXME
    pass

#Bonus: and with the binary structure?

def dfsasbin2(B):
    #FIXME
    pass

"""
Breadth First Search
"""


# first version: a "end level mark" (None) is add in the queue

def bfs(T):
    """
    returns the width of T
    """
    #FIXME
    pass

#second version: two queues + displays keys by levels...

def bfsasbin(B):
    #FIXME
    pass
