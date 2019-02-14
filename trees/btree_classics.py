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
    if B.children is None:
        return B.keys[-1]
    else:
        return maxBTree(B.children[-1])
    
def __binarySearchPos(L, x, left, right):
    # FIXME
    pass


def binarySearchPos(L, x):
    """
    returns the position where x is or might be in L
    """
    return __binarySearchPos(L, x, 0, len(L))


def __searchBtree(B, x):
    #FIXME
    pass


def searchBTree(B, x):
    return None if not B else __searchBtree(B, x)



    
