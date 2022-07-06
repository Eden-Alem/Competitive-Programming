# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head -> head.next -> ..... -> tail
# 1 -> 2 > 3 > 4 > 5
# 1 > 2 > 3 > 4 > 5 > null 

# [1,2,3,4,5]
# [5,4,3,2,1]
# 5 > 4 > 3 > 2 >1
# O(2n) > time complexity
# O(n) > space complexity


# null 1 2 3 4 5
#      | |
    

# 5 2 3 4 1
#  |      |

# 5 4  3  2 1
#   | ||  |
    
# null < 1 < 2 < 3 < 4 < 5  null
                         # |      |
                         # v      h
        # null 1> null  
        #      |       |
        # []
        # [1]
        # [2,3,4,5,6]
# 1.next = 2 --- savedHead
# 1 > null
# 2.next = 3
# savedHead 2 > 1 > null

# Space complexity: O(1)
# time complexity; O(n)

    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = None 
        temp = None
        
        while head:  
            temp = head.next   # 2>3>4>5; crosscheck
            head.next = value  # 1>null
            value = head
            head = temp 
            
            
        return value
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        