# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        p = dummy

        while p.next != None:
            if p.next.next != None:
                temp = p.next
                p.next = p.next.next
                temp.next = p.next.next
                p.next.next = temp
                p = p.next.next
            else:
                p = p.next
        return dummy.next


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


list = [1]
head = creat_listnode(list)
a = Solution().swapPairs(head)