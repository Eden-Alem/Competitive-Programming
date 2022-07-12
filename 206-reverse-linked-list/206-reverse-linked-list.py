# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#          |
#      1 2 n
# null   |
#          |     
#                | 

#       2 > 1 > n
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = right = None
        while head:
            right = head.next
            head.next = left
            left = head
            head = right
            
        return left
            
            
    