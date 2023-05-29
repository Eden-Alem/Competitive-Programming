# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = fast = dummyHead = ListNode(0, head)

        while fast:
            if (n < 0):
                slow = slow.next
                
            fast = fast.next
            n -= 1

        slow.next = slow.next.next if slow.next else None

        return dummyHead.next


