"""
Solution
"""

from node import Node

def reverse(head: Node) -> Node:
    """ Recursivly reverses a linked list.
    """

    if not head:
        return None

    if not head.next:
        return head

    node = reverse(head.next)
    head.next.next = head
    head.next = None

    return node
