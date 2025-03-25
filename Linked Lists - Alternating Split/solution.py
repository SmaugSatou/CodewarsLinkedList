"""
Solution
"""

from node import Node

class Context(object):
    """
    Context class
    """

    def __init__(self, first: Node, second: Node):
        self.first = first
        self.second = second

def alternating_split(head: Node) -> Context:
    """ Splits a linked list into two linked lists.
    """

    if not head or not head.next:
        raise ValueError()

    first_dummy = Node(-1)
    second_dummy = Node(-1)

    to_first = True

    first_curr = first_dummy
    second_curr = second_dummy

    while head:
        if to_first:
            first_curr.next = Node(head.data)
            first_curr = first_curr.next
        else:
            second_curr.next = Node(head.data)
            second_curr = second_curr.next

        head = head.next
        to_first = not to_first

    return Context(first_dummy.next, second_dummy.next)
