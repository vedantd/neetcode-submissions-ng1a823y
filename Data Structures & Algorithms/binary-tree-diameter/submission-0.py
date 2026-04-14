# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def depth(node:Optional[TreeNode]):
            if node == None:
                return 0
            
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            self.max_diameter = max(self.max_diameter,l_depth + r_depth)

            h= 1 + max(l_depth,r_depth)

            return h

        
       
        
        depth(root)
        return self.max_diameter
        
