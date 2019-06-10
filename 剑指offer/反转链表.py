# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

class Solution:
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        p1 = None
        p2 = pHead
        if p2.next != None:
            p3 = p2.next
        else:
            return pHead

        while p3 != None:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
        p2.next = p1
        return p2


list1 = [1, 2, 3, 4, 5]
head = creat_listnode(list1)
p2 = Solution().ReverseList(head)

