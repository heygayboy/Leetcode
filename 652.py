# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

import collections


class Node(object):
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()

    def CreatTree(self, data):
        if (data == 0):
            return None

        temp = Node()

        temp.data = data
        print("{0}->left".format(data))
        t = input()
        temp.lchild = self.CreatTree(t)
        print("{0}->right".format(data))
        t = input()
        temp.rchild = self.CreatTree(t)
        return temp

    def pre(self,root):
        if(root == None):
            return
        print("{0}".format(root.data), end = '')
        self.pre(root.lchild)
        self.pre(root.rchild)


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        m = collections.defaultdict(int)
        self.helper(root, m, res)
        return res

    def helper(self, root, m, res):
        if not root:
            return '#'
        path = str(root.data) + ',' + self.helper(root.lchild, m, res) + ',' + self.helper(root.rchild, m, res)
        if m[path] == 1:
            res.append(root)
        m[path] += 1
        return path

if __name__ == '__main__':
    root = Node()
    tree = Tree()
    root = tree.CreatTree(1)
    Solution = Solution()
    res = Solution.findDuplicateSubtrees(root)
