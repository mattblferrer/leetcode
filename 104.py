# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        if not root:  # empty root edge case
            return 0
        if not root.left and not root.right:  # reached leaf node
            return 1
        if not root.left: 
            return 1 + self.maxDepth(root.right)
        if not root.right:
            return 1 + self.maxDepth(root.left)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))