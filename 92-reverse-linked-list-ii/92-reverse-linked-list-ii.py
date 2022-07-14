# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        dummyHead = subHead = ListNode(0, head)
        for _ in range(1, left):
            subHead = subHead.next
        
        reverseStart = subHead.next
        for _ in range(right - left):
            temp = reverseStart.next
            reverseStart.next, temp.next, subHead.next = temp.next, subHead.next, temp
            
        return dummyHead.next
        
            
            
        
        