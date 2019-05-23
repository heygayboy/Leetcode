class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        return self.sym(root.left, root.right)

    def sym(self, left, right):
        if left == None and right == None:
            return True
        if (left == None) ^ (right == None):
            return False
        if left.val == right.val:
            return self.sym(left.left, right.right) and self.sym(left.right, right.left)