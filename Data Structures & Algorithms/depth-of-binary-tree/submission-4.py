# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        if root is None:
            return 0
        
        l_hieght = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)

        hmax = 1 + max(l_hieght, r_height)
        return hmax




        