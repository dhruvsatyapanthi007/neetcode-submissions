# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        self.traverse(root, 0)

        return self.res

    def traverse(self, root, level):
        if not root:
            return

        if len(self.res) == level:
            self.res.append([])

        self.res[level] = root.val

        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
