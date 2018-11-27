# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = 0
        h = head
        while h != None:
            h = h.next
            length = length + 1
        k = k % length
        p1 = head
        p2 = p1
        for i in range(k):
            p2 = p2.next

        while p2.next != None:
            p1 = p1.next
            p2 = p2.next

        p3 = head
        p2.next = head
        new_head = p1.next
        p1.next = None
        return new_head


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


list1 = [1, 2, 3, 4, 5]
head = creat_listnode(list1)
k = 2
a = Solution().rotateRight(head, k)