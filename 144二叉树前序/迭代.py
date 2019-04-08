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

        def pre(root):
            if not root:
                return
            res.append(root.val)
            pre(root.left)
            pre(root.right)

        res = []
        pre(root)
        return res
