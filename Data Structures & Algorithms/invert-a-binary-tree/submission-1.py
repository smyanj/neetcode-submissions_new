# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root:
                root.left, root.right = root.right, root.left
                    

        if not root:
            return None

        dfs(root)
        dfs(root.left)
        dfs(root.right)
        

        return root
    
            

        