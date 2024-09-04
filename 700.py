# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # type: ignore
        if val == root.val:  # value found
            return root
        else:
            if not root.left and not root.right:  # searched without match
                return None
            elif root.right and val > root.val:  # search on right node
                return self.searchBST(root.right, val)
            elif root.left and val < root.val:  # search on left node
                return self.searchBST(root.left, val)