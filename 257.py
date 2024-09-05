# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: # type: ignore
        if not root.left and not root.right:  # leaf reached
            return [str(root.val)]
            
        new_paths = []
        if root.left:  # traverse left node for paths
            left_paths = self.binaryTreePaths(root.left)
            for path in left_paths:  # append root to paths found
                new_path = str(root.val) + "->" + path
                new_paths.append(new_path)

        if root.right:  # traverse right node for paths
            right_paths = self.binaryTreePaths(root.right)
            for path in right_paths:  # append root to paths found
                new_path = str(root.val) + "->" + path
                new_paths.append(new_path)

        return new_paths