# -*- coding:utf-8 -*-
list1 = []
list2 = []


class Solution:

    def push(self, node):
        # write code here

        list2.append(node)

    def pop(self):
        # return xx
        while list2 != []:
            list1.append(list2.pop())
        a = list1.pop()
        while list1 != []:
            list2.append(list1.pop())
        return a

