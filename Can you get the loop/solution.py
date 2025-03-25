"""
Solution
"""

from node import Node

def loop_size(node: Node) -> int:
    """ Calculates loop size in a linked list
    """

    fast = node
    slow = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:       
            res = 1
            curr_node = slow.next

            while slow != curr_node:
                res += 1
                curr_node = curr_node.next

            return res

    return 0
