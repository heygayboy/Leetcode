# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        p1 = None
        p2 = None

        while p != None:
            if p.val < x:
                if not p1:
                    p1 = p
                else:
                    p1.next = p
                    p1 = p1.next
            else:
                if not p2:
                    p2 = p
                    head2 = p2
                else:
                    p2.next = p
                    p2 = p2.next
            p = p.next

        p1.next = head2
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


list = [1, 4, 3, 2, 5, 2]
head = creat_listnode(list)
a = Solution().partition(head, 3)