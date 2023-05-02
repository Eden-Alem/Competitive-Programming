# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        curr = head
        prev = dummyNode
        
        while(curr and curr.next):
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            
            curr = curr.next
            prev = prev.next.next
        
        return dummyNode.next
            