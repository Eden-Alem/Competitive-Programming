# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        end = None
        if stack:
            end = stack[-1]
            
        while stack:
            element = stack.pop()
            if stack:
                element.next = stack[-1]
            else:
                element.next = None
                
        return end