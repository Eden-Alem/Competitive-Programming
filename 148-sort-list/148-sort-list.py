# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def merge(n1, n2):
            result = node = ListNode()
            
            while n1 and n2:
                if n1.val > n2.val:
                    node.next = ListNode(n2.val)
                    n2 = n2.next
                else:
                    node.next = ListNode(n1.val)
                    n1 = n1.next
                    
                node = node.next
                
            node.next = n1 or n2
            
            return result.next
                    
        
        def mergeSort(s, e):
            if s == e:
                return ListNode(s.val)
            
            slow = s
            fast = s
            while fast.next != e:
                slow = slow.next
                fast = fast.next
                if fast.next != e:
                    fast = fast.next
                    
            n1 = mergeSort(s, slow)
            n2 = mergeSort(slow.next, e)
            
            return merge(n1, n2)
            
        last = head
        while last.next:
            last = last.next
            
        return mergeSort(head, last)
        