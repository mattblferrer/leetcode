# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        if not p and not q:  # both empty trees
            return True
        if not p or not q:  # only one empty tree
            return False
        if p.val != q.val:  # check if values match
            return False
            
        is_same = True
        if p.left and q.left:  # check left subtree if same
            is_same &= self.isSameTree(p.left, q.left)
        elif (not p.left and q.left) or (p.left and not q.left):
            return False
        if p.right and q.right:  # check right subtree if same
            is_same &= self.isSameTree(p.right, q.right)
        elif (not p.right and q.right) or (p.right and not q.right):
            return False

        return is_same