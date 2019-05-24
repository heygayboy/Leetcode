# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        flag = 1
        parents_queue = []
        children_queue = []
        result = []
        temp = []

        if root == None:
            return parents_queue
        else:
            parents_queue.append(root)

        while (parents_queue != [] or children_queue != []):
            node = parents_queue.pop(0)
            temp.append(node.val)

            if node.left != None:
                children_queue.append(node.left)
            if node.right != None:
                children_queue.append(node.right)

            if parents_queue == []:
                result.append(temp)
                temp = []
                parents_queue = children_queue
                children_queue = []

        return result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        flag = 1
        parents_queue = []
        children_queue = []
        result = []
        temp = []

        if root == None:
            return parents_queue
        else:
            parents_queue.append(root)

        while (parents_queue != [] or children_queue != []):
            node = parents_queue.pop(0)
            temp.append(node.val)

            if node.left != None:
                children_queue.append(node.left)
            if node.right != None:
                children_queue.append(node.right)

            if parents_queue == []:
                result.append(temp)
                temp = []
                parents_queue = children_queue
                children_queue = []

        return result

