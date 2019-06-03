# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin:
            return None
        if len(pre) == 1 or len(tin) == 1:
            rootval = pre[0]
            Lroot = TreeNode(rootval)
            Lroot.left = None
            Lroot.right = None
            return Lroot

        rootval = pre[0]
        root_index = tin.index(rootval)
        if root_index != 0:
            left_tin = tin[0: root_index]
            left_pre = pre[1: 1 + len(left_tin)]
        else:
            left_tin = []
            left_pre = []

        if root_index != len(pre)-1:
            right_tin = tin[root_index + 1:]
            right_pre = pre[1 + len(left_tin):]
        else:
            right_tin = []
            right_pre = []

        root = TreeNode(rootval)
        root.left = self.reConstructBinaryTree(left_pre, left_tin)
        root.right = self.reConstructBinaryTree(right_pre, right_tin)

        return root

pre = [1,2,3,4,5,6,7]
tin = [3,2,4,1,6,5,7]
a = Solution().reConstructBinaryTree(pre,tin)