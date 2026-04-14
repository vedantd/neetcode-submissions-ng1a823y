# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.g_max = 0
        def dfs(curr):
            if curr is None:
                return 0
            
            h_l = dfs(curr.left)
            h_r = dfs(curr.right)
            diam_at_node = h_l + h_r
            
            self.g_max =  max(self.g_max , diam_at_node)
            return 1 + max(h_l , h_r)
        dfs(root)

        return self.g_max

        
       

        


       



        


        