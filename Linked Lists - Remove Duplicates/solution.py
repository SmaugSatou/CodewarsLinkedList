"""
Solution
"""

from node import Node

def remove_duplicates(head: Node) -> Node:
    """ Removes duplicates from linked list.
    """

    curr_node = head

    while curr_node:
        next_node = curr_node.next

        while next_node and next_node.data == curr_node.data:
            next_node = next_node.next

        curr_node.next = next_node
        curr_node = next_node

    return head
