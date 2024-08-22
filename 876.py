# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head  # left and right pointers
        try:
            while right.next:
                left, right = left.next, right.next.next
        except AttributeError:  # if right.next does not exist
            return left
        return left