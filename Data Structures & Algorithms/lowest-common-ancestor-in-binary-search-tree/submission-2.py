# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        self.p = p
        self.q = q

        _, _ = self.traverse(root)

        return self.res

    def traverse(self, root: TreeNode) -> [bool, bool]:
        if not root:
            return False, False

        leftSubTreeContainsP, leftSubTreeContainsQ = self.traverse(root.left)
        rightSubTreeContainsP, rightSubTreeContainsQ = self.traverse(root.right)

        containsP = root == self.p or leftSubTreeContainsP or rightSubTreeContainsP
        containsQ = root == self.q or leftSubTreeContainsQ or rightSubTreeContainsQ

        if containsP and containsQ and not self.res:
            self.res = root

        return containsP, containsQ
