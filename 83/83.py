# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if not p:
            return None

        while p!= None:
            while p.next != None and p.val == p.next.val:
                p.next = p.next.next
            p = p.next

        return head

class ListNode(object):
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

list = [1,1,1]
head = creat_listnode(list)
a = Solution().deleteDuplicates(head)