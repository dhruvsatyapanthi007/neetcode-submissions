# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.traverse(root)

        return self.res

    def traverse(self, root):
        if not root:
            return 0

        leftNodeHeight = self.traverse(root.left)
        rightNodeHeight = self.traverse(root.right)

        diff = leftNodeHeight - rightNodeHeight

        self.res &= abs(diff) <= 1

        return max(leftNodeHeight, rightNodeHeight) + 1
        