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
            while root:
                if root.left and root.right:
                    root.left, root.right = root.right, root.left

                root = root.right

        if not root:
            return None

        main = dfs(root)
        l = dfs(root.left)

        return root
    
            

        