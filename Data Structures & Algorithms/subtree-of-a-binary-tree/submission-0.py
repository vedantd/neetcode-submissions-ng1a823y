# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(t,subR):
            if not t and not subR:
                return True
            if not t or not subR:
                return False
        
            if t.val != subR.val:
                return False
            return sameTree(t.left, subR.left) and sameTree(t.right, subR.right)
        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
        

        

        
        