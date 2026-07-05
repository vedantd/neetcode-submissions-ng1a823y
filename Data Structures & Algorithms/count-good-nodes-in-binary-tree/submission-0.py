# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(node, maxv):
            if not node:
                return 0
            
            
            if node.val >= maxv:
                self.res += 1
            
            
            new = max(maxv,node.val)
            dfs(node.left, new) 
            dfs(node.right, new)
        dfs(root, float("-inf"))
        return self.res