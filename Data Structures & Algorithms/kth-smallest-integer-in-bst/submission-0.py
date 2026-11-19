# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = root.val

        self.traverse(root)

        return self.res

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        self.count += 1

        if self.count == k:
            self.res = root.val

        self.traverse(root.right)