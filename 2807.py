# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from math import gcd 

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        first = head  # store head of linked list before insertion
        while head.next:
            new_node = ListNode(gcd(head.val, head.next.val)) # type: ignore
            head.next, new_node.next = new_node, head.next
            head = head.next.next  # skip after newly inserted node

        return first