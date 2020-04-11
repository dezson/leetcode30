# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def dfs(root):
            if root is None:
                return 0
            r = dfs(root.right)
            l = dfs(root.left)
            self.ans = max(self.ans, r+l+1)
            return max(r,l)+1
            
        dfs(root)
        return self.ans-1
