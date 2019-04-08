#coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''建立一棵树'''
class Tree(object):
    def __init__(self):
        self.root = TreeNode()

    def CreatTree(self, data):
        if (data == 0):
            return None

        temp = TreeNode()

        temp.data = data
        print("{0}->left".format(data))
        t = input()
        temp.lchild = self.CreatTree(t)
        print("{0}->right".format(data))
        t = input()
        temp.rchild = self.CreatTree(t)
        return temp



class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while(root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

root = Tree.CreatTree(1)
res = Solution().inorderTraversal(root)