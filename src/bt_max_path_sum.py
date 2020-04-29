# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.summ = float('-inf')
        def dfs(root, summ):
            if root is None:
                return 0
            left = max(0, dfs(root.left, summ))
            right = max(0, dfs(root.right, summ))
            self.summ = max(self.summ, left+right+root.val)
            return max(left ,right)+root.val

        dfs(root,root.val)
        return self.summ
