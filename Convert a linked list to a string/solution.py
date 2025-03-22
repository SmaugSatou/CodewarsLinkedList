"""
Solution
"""

from node import Node

def stringify(node: Node) -> str:
    """ Converts a linked list to a string
    """

    result = ""

    while node:
        result += str(node.data) + " -> "
        node = node.next

    return result + "None"
