# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        if not root:  # no root node
            return 0 
        elif not root.left and not root.right:  # leaf node reached
            return 1
        elif not root.left:  # no left node
            return 1 + self.minDepth(root.right)
        elif not root.right:  # no right node
            return 1 + self.minDepth(root.left)
        # has left and right node
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))