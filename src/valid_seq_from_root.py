# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root, idx, arr):
            if root is None:
                return False

            if root.val == arr[idx]:
                if idx == len(arr)-1:
                    if root.right is None and root.left is None:
                        return True
                    else:
                        return False
                return dfs(root.right,idx+1,arr) or dfs(root.left,idx+1,arr)
            else:
                return False


        return dfs(root,0,arr)
