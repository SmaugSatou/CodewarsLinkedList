"""
Node class
"""

class Node:
    """ 
    Node of linked list representation
    """
    def __init__(self, data, next: "Node" = None):
        self.data = data
        self.next = next
