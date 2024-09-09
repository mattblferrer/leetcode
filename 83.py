# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        first = head  # assign head of entire linked list
        try: 
            while head.next:
                while head.val == head.next.val:
                    head.next = head.next.next
                head = head.next

        except AttributeError:  # if no more elements in linked list
            return first
        return first  # if no error, still output head