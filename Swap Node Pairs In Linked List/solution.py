"""
Solution
"""

from node import Node

def swap_pairs(head: Node) -> Node:
    """ Swap each pair of nodes in a linked list.
    """

    dummy = Node(-1)
    dummy.next = head

    prev_node = dummy

    while head and head.next:
        swap_node = head.next
        next_node = swap_node.next

        prev_node.next = swap_node
        swap_node.next = head
        head.next = next_node

        prev_node = head
        head = next_node

    return dummy.next
