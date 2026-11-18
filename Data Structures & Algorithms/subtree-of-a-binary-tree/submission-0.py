# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        self.subRoot = subRoot
        self.traverse(root)

        return self.res

    def traverse(self, root) -> None:
        if not root:
            return

        self.res = self.res or self.isSame(root, self.subRoot)

        self.traverse(root.left)
        self.traverse(root.right)

    def isSame(self, p, q) -> bool:
        if not p:
            return not q
        elif not q:
            return not p
        else:
            return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
