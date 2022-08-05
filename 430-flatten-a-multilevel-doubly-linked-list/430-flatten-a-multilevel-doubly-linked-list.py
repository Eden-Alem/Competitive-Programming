"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def __init__(self):
        self.stack = deque()

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        resultHead = head
        node = self.builder(head)
        while len(self.stack):
            val = self.stack.pop()
            if val:
                node.next = val
                val.prev = node
                node = self.builder(val)

        return resultHead

    def builder(self, node):
        while node and (node.next or node.child):
            if node.child:
                self.stack.append(node.next)
                node.next = node.child
                node.child.prev = node
                node.child = None
            node = node.next
        return node
        