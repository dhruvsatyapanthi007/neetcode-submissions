# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        self.traverse(root)

        return self.res

    def traverse(self, root):
        if not root:
            return None, None

        minLeft, maxLeft = self.traverse(root.left)
        minRight, maxRight = self.traverse(root.right)

        if minLeft is None:
            minValue = root.val
        else:
            self.res = self.res and maxLeft < root.val
            minValue = min(minLeft, root.val)
        
        if maxRight is None:
            maxValue = root.val
        else:
            self.res = self.res and root.val < minRight
            maxValue = max(maxRight, root.val)

        return minValue, maxValue
