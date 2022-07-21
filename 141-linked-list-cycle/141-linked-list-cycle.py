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
        slow = None
        fast = None
        visited = set()
        
        while head:
            slow = head
            fast = head.next
            visited.add(slow)
            
            if fast in visited:
                return True
            
            head = head.next
            
        return False
        