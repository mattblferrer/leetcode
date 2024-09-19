# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        seen = set()
        while head:  # check every node if encountered previously
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        
        return None  # no duplicate node found
        