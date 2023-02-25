"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        reference = { None: None }
        
        node = head
        while node:
            reference[node] = Node(node.val)
            node = node.next
            
        node = head
        while node:
            new_node = reference[node]
            new_node.next = reference[node.next]
            new_node.random = reference[node.random]
            node = node.next
            
        return reference[head]
        
        