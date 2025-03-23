"""
Solution
"""

from node import Node

def sorted_insert(head: Node, data: int):
    """ Inserts node by value.
    """

    new_node = Node(data)

    if not head:
        return new_node

    if head.data >= data:
        new_node.next = head
        return new_node

    curr_node = head
    while curr_node.next and curr_node.next.data < data:
        curr_node = curr_node.next

    new_node.next = curr_node.next
    curr_node.next = new_node

    return head
