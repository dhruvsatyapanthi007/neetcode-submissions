# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.traverse(root, -math.inf)

        return self.res
        
    def traverse(self, root, currMax):
        if not root:
            return None

        self.res += int(currMax <= root.val)

        currMax = max(currMax, root.val)

        self.traverse(root.left, currMax)
        self.traverse(root.right, currMax)
