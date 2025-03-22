"""
Solution
"""

from node import Node

class Context(object):
    """
    Pair of linked list.
    """

    def __init__(self, source: Node, dest: Node):
        self.source = source
        self.dest = dest

def move_node(source: Node, dest: Node) -> Context:
    """ Moves front node of source to front of dest linked list.
    """

    if not source:
        raise ValueError()

    target_node = source
    source = source.next

    target_node.next = dest
    dest = target_node

    return Context(source, dest)
