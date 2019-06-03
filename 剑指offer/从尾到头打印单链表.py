# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead1(self, listNode):
        '''
        通过翻转列表实现的
        :param listNode:
        :return:
        '''
        # write code here
        p = listNode
        list_num = []

        while p != None:
            list_num.append(p.val)
            p = p.next

        return list(reversed(list_num))



#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        '''
        通过递归实现先打印最后一个
        :param listNode:
        :return:
        '''
        if not listNode:
            return []

        list_num = []
        global list_num

        if listNode == None:
            return

        list_num = self.printListFromTailToHead(listNode.next)
        list_num.append(listNode.val)
        return list_num