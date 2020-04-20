class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        def insertBst(tree, val):
            if tree is None:
                tree.val = val

            if val < tree.val:
                if tree.left is not None:
                    insertBst(tree.left, val)
                else:
                    tree.left = TreeNode(val)
            else:
                if tree.right is not None:
                    insertBst(tree.right, val)
                else:
                    tree.right = TreeNode(val)


        root = TreeNode(preorder[0])
        for x in range(1,len(preorder)):
            insertBst(root, preorder[x])
        return root

