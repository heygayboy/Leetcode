# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root or stack:
            while not root:
                res.append(root.left)
                stack.append(root.right)
                root = root.left
            root = stack.pop()
            res.append(root.left)
            root = root.right
        return res
