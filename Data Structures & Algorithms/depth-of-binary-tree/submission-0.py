# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            maxD = 1
            if not curr:
                return 0
            
            while curr:
                maxl = 1
                maxr = 1
                if curr.left:
                    maxl += 1
                if curr.right:
                    maxr += 1
                maxd = max(maxr, maxl)
                curr = curr.right
                
                
                
            return 1 + maxd

        return dfs(root)