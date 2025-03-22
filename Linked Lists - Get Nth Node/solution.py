"""
Solution
"""

from node import Node

def get_nth(node: Node, index: int) -> Node:
    """ Gets node by index.
    """

    if not node:
        raise ValueError()

    if index < 0:
        raise IndexError()

    for _ in range(index):
        if not node.next:
            raise IndexError()

        node = node.next

    return node
