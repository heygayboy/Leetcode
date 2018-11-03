# -*- coding: utf-8 -*-


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

'''
翻转链表
翻转链表需要三个指针
两个指针用于指向翻转顺序，另一个指针用于指出下一个的翻转对象
'''


def reverse_Listnode(head):
    if head == None:
        return None

    elif head.next == None:
        return head

    else:
        p = head
        q = p.next
        while q != None:
            r = q.next
            q.next = p
            p = q
            q = r
        head.next = None
        return p

def reverseKGroup(head, k):
    p1 = head
    #断开K个节点，p2用于表明结尾位置 p1用于移动记下K节点链表节点数
    for i in range(k):
        if p1 == None:
            return head
        p2 = p1
        p1 = p1.next
    p2.next = None

    #翻转K节点的链表 此时head从链表头指针变为链表尾指针 result从链表尾指针变为链表头指针
    result = reverse_Listnode(head)

    #递归
    head.next = reverseKGroup(p1, k)
    return result


list1 = [1,2,3,4,5]
head = creat_listnode(list1)
b = reverseKGroup(head, 3)