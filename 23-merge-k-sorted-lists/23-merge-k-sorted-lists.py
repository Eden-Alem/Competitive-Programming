# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for head in lists:
            while head:
                heapq.heappush(array, head.val)
                head = head.next
                
        node = dummy_node = ListNode()
        while array:
            a = heapq.heappop(array)
            dummy_node.next = ListNode(a)
            dummy_node = dummy_node.next
            
        return node.next
        