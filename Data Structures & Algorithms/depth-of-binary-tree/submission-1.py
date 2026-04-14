# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        
        h_left = 1 +  self.maxDepth(root.left)
        h_right = 1 +  self.maxDepth(root.right)


        curr = max(h_left,h_right)

        return curr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if root == None:
        #     return 0
        
        # h_left = self.maxDepth(root.left)
        # h_right = self.maxDepth(root.right)

        # h_total = 1 + max(h_left,h_right)

        # return h_total

        