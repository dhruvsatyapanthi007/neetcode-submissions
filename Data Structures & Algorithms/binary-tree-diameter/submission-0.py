# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traverse(root)

        return self.res

    def traverse(self, root):
        if not root:
            return 0

        leftNodeHeight = self.traverse(root.left)
        rightNodeHeight = self.traverse(root.right)

        self.res = max(self.res, leftNodeHeight + rightNodeHeight)

        return max(leftNodeHeight, rightNodeHeight) + 1
