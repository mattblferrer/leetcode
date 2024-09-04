# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool: # type: ignore
        if not root.left:  # reached leaf node
            return root.val
        if root.val == 2:  # OR
            return self.evaluateTree(root.left) | self.evaluateTree(root.right)
        elif root.val == 3:  # AND
            return self.evaluateTree(root.left) & self.evaluateTree(root.right)