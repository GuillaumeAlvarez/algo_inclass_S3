#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S3 - API
B-Trees: classics (research, insertions, suppressions)
"""

from algopy import btree



def minBTree(B):
    """
    B != None
    """
    while B.children:
        B = B.children[0]
    return B.keys[0]

def maxBTree(B):
    if B.children == []:
        return B.keys[-1]
    else:
        return maxBTree(B.children[-1])
    
def __binarySearchPos(L, x, left, right):
    if left == right:
        return left
    else:
        mid = left + (right - left) // 2
        if x == L[mid]:
            return mid
        elif x < L[mid]:
            return __binarySearchPos(L, x, left, mid)
        else:
            return __binarySearchPos(L, x, mid+1, right)

def binarySearchPos(L, x):
    """
    returns the position where x is or might be in L
    """
    return __binarySearchPos(L, x, 0, len(L))

def __searchBtree(B, x):
    i = binarySearchPos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return (B, i)
    else:
        if B.children == []:
            return None
        else:
            return __searchBtree(B.children[i], x)

def searchBTree(B, x):
    return None if not B else __searchBtree(B, x)


# 2.3 insertion

def split(B, i):
    '''
    splits the child i of B
    conditions:
    - B is a nonempty tree and its root is not a 2t-node.
    - The child i of B exists and its root is a 2t-node.
    '''
    
    L = B.children[i]
    R = btree.BTree()
    mid = B.degree-1
    # keys
    (L.keys, x, R.keys) = (L.keys[:mid], L.keys[mid], L.keys[mid+1:])
    # children    
    if L.children == []:
        R.children = [] # useless L[:2] = [] if L is []!
    else:   
        (L.children, R.children) = (L.children[:mid+1], L.children[mid+1:])
    # root            
    B.keys.insert(i, x)
    B.children.insert(i+1, R)



def __insert(B, x):
    '''
    conditions:
    - B is a nonempty tree 
    - its root is not a 2t-node
    returns: True if the insertion occurs (only to make code clearer... not used!)
    There is no need to return B, the root (the reference) does not change!
    '''    
    i = binarySearchPos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return False
    elif B.children == []: # leaf
        B.keys.insert(i, x)
        return True
    else:
        if B.children[i].nbkeys == 2 * B.degree - 1:
            if B.children[i].keys[B.degree-1] == x:
                return False
            split(B, i)
            if x > B.keys[i]:
                i += 1
        return __insert(B.children[i], x)
        
def insert(B, x):
    '''
    inserts x in B (if not already in B)
    returns B (needed: in case of new root!)
    '''
    
    if B ==  None:        
        return btree.BTree([x])
    else:
        if B.nbkeys == 2 * B.degree - 1:    # root split
            B = btree.BTree([], [B])
            split(B, 0)
        __insert(B, x)
        return B
