# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 3 2 0 4
#       |
#   |

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        
        while head:            
            if head in visited:
                return head
            
            visited.add(head)
            
            head = head.next
            
        return None
        