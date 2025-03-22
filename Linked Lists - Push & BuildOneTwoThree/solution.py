"""
Solution
"""

from node import Node

def push(head, data):
    """ Pushes node to linked list
    """

    if not head:
        return Node(data)

    node_next = head
    head = Node(data)
    head.next = node_next

    return head

def build_one_two_three():
    """ Build linked list of form 1->2->3->None
    """

    head = None

    for i in range(3, 0, -1):
        head = push(head, i)

    return head
