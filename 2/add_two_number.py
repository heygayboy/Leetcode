
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = None

        carry = 0
        p = l1
        q = l2
        head = dummy

        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum / 10

            r = ListNode(sum % 10)
            r.next = None
            dummy.next = r
            dummy = r

            if p:
                p = p.next
            else:
                p = None

            if q:
                q = q.next
            else:
                q = None

        if carry:
            r = ListNode(carry)
            r.next = None
            dummy.next = r
            dummy = r

        result = head.next
        return result


def creat_listnode(list):
    head = ListNode(list[0])
    head.next = None
    listnode = head
    for num in list[1:]:
        tempnode = ListNode(num)
        tempnode.next = None
        listnode.next = tempnode
        listnode = tempnode
    return head


l1list = [1, 8]
l1 = creat_listnode(l1list)
l2list = [0]
l2 = creat_listnode(l2list)
Solution = Solution()
result = Solution.addTwoNumbers(l1, l2)