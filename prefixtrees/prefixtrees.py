__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixTrees.py 2019-02-18'

"""
Prefix Trees homework
2019
@author: login
"""


from algopy import tree


################################################################################
## MEASURES
                        
def countwords(T):
    """ count words in dictionnary T
    
    :param T: The prefix tree
    :rtype: int
    """

    # FIXME
    pass

def longestwordlength(T):
    """ longest word length
    
    :param T: The prefix tree
    :rtype: int
    """
    
    # FIXME
    pass

def averagelength(T):
    """ average word length
    
    :param T: The prefix tree
    :rtype: float
    """
    
    # FIXME
    pass

###############################################################################
## Researches


def searchword(T, word):
    """ search for a word in dictionary
    
    :param T: The prefix tree
    :param word: The word to search for
    :rtype: bool
    """
    
    # FIXME
    pass

###############################################################################
## Lists

def wordlist(T):
    """ generate the word list
    
    :param T: The prefix tree
    :rtype: list
    """
    
   # FIXME
    pass

def longestwords(T):
    """ search for the longest words in dictionary
    
    :param T: The prefix tree
    :rtype: list
    """
    
    # FIXME
    pass
    
def completion(T, prefix):
    """ generate the list of words with a common prefix
    
    :param T: The prefix tree
    :param pref: the prefix
    :rtype: list
    """
    
    # FIXME
    pass

def treetofile(T, filename):
    """ save the dictionary in a file
    
    :param T: The prefix tree
    :param filename: the file name
    """
    
    #FIXME
    pass


###############################################################################
## Build Tree

def addword(T, word):
    """ add a word in dictionary
    
    :param T: The prefix tree
    :param word: The word to add
    """
    
    # FIXME
    pass

def treefromfile(filename):
    """ build the prefix tree from a file of words
    
    :param filename: The file name
    :rtype: Tree
    """
    
    # FIXME
    pass
