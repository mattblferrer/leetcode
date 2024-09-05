# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: # type: ignore
        if root == None:
            return False
        if root.val == targetSum:  # path found that equals targetSum
            if not root.left and not root.right:  # check if leaf
                return True
        return (self.hasPathSum(root.left, targetSum - root.val) 
            or self.hasPathSum(root.right, targetSum - root.val))