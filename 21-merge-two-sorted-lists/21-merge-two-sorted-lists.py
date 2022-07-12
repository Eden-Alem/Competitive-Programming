# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# null 1 1 2 3 4 4 => return dummy.next
#                |

# if one list finishes early:
#     Make sure to have the next of the dummy node's tail point to whichever existing list (not null list)
    
# 1 2 4 null -> list1
#        |

# 1 3 4 6 7 8 null -> list2
#     |

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = tailNode = ListNode() # null
        while list1 and list2:
            if list1.val <= list2.val:
                tailNode.next = list1
                list1 = list1.next
            else:
                tailNode.next = list2
                list2 = list2.next
            tailNode = tailNode.next
        
        tailNode.next = list1 or list2
            
        return dummyHead.next
        