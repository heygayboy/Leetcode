# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def zhongxu(root):
            if root == None:
                return
            zhongxu(root.left)
            res.append(root.val)
            zhongxu(root.right)

        res = []
        zhongxu(root)
        return res

