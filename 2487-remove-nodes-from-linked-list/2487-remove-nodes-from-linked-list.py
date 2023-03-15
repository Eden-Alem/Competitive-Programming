# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
      
        monotonic = []
        
        for i in range(len(arr)):
            while monotonic and monotonic[-1] < arr[i]:
                monotonic.pop()
                
            monotonic.append(arr[i])
        
        result_head = new_head = ListNode()
        for val in monotonic:
            new_head.next = ListNode(val)
            new_head = new_head.next
            
        return result_head.next
            
        
        