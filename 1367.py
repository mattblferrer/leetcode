# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool: # type: ignore
        def checkPathExists(head, root) -> bool:
            if head.val == root.val:  # check if downward path can be formed
                if not head.next:
                    return True
                if root.left and root.left.val == head.next.val:  # check left
                    if checkPathExists(head.next, root.left):
                        return True
                if root.right and root.right.val == head.next.val:  # check right
                    if checkPathExists(head.next, root.right):
                        return True
            return False

        is_sub_path = checkPathExists(head, root)
        if is_sub_path:
            return True

        # check downward paths in left, right subnodes
        if root.left:  # check left
            is_sub_path |= self.isSubPath(head, root.left)
        if root.right:  # check right
            is_sub_path |= self.isSubPath(head, root.right)
        return is_sub_path