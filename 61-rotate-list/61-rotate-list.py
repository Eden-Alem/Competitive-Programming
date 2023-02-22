# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length, tail = 1, head
        
        while tail.next:
            tail = tail.next
            length += 1
            
        k = k % length
        if k == 0:
            return head
        
        n = length - k - 1
        
        cur_node = head
        for i in range(n):
            cur_node = cur_node.next
            
        new_head = cur_node.next
        cur_node.next = None
        
        tail.next = head
        
        return new_head