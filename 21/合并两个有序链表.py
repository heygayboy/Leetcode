# -*- coding: utf-8 -*-

# Definition for singly-linked list.
'''
使用非递归的方式
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        head = None
        p1 = l1
        p2 = l2

        if(l1.val < l2.val):
            head = l1
            p1 = l1.next
        else:
            head = l2
            p2 = l2.next

        result = head

        while(p1 and p2):
            if p1.val < p2.val:
                result.next = p1
                p1 = p1.next
            else:
                result.next = p2
                p2 = p2.next
            result = result.next
        if p1:
            result.next = p1
        elif p2:
            result.next = p2

        return head


def creat_listnode(list):
    dummy = ListNode(0)
    dummy.next = None

    dum = dummy
    for value in (list):
        temp = ListNode(value)
        temp.next = None
        dum.next = temp
        dum = temp

    head = dummy.next
    return head


list1 = [1, 2, 4]
list2 = [1, 3, 4]
l1 = creat_listnode(list1)
l2 = creat_listnode(list2)
a = Solution().mergeTwoLists(l1, l2)
