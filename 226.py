# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        if not root:  # edge case for empty node
            return None
        root.left, root.right = root.right, root.left  # invert left and right
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root