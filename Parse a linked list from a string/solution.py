"""
Solution
"""

from node import Node

def linked_list_from_string(s: str) -> Node:
    """ Parses linked list from string
    """

    dummy = Node(None)

    nodes = s.split(" -> ")[:-1]

    curr_node = dummy
    for node in nodes:
        curr_node.next = Node(int(node))
        curr_node = curr_node.next

    return dummy.next
