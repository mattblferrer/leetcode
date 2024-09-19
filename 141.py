# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore
        if not head:  # edge case of empty linked list
            return False

        slow, fast = head, head.next  # slow and fast pointers
        while slow.next:
            if slow == fast:  # if no cycle, slow always behind fast
                return True
            if not fast or not fast.next:  # fast pointer reached end of list 
                return False
            slow, fast = slow.next, fast.next.next

        return False