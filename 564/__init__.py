# -*- coding: utf-8 -*-
from __future__ import print_function


'''

给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。
“最近的”定义为两个整数差的绝对值最小。

'''

n = '11011'

length = len(n)
border_a = ['9'] * (length-1)
border_b = ['1'] * int(length / 2) + ['0'] + ['1'] * int(length / 2)

p = list()

for i in range(int(length / 2)):
    p.append(n[i])

if length % 2 == 0:
    for i in reversed(range(len(p))):
        p.append(p[i])
else:
    p.append(n[int(length / 2)])
    for i in reversed(range(len(p) - 1)):
        p.append(p[i])

str4 = "".join(p)

if str4 == n:
    if length % 2 ==0:
        for index in reversed(range(len(p))):
            p[index] = str(int(p[index]) - 1)
    else:
        index = int(length/2)
        p[index] = str(int(p[index]) - 1)

str4 = "".join(p)

if border_a != []:
    border1 = int("".join(border_a))
    border2 = int("".join(border_b))
    list_num = [border1, border2, int(str4)]
    min = int(n)
    for num in list_num:
        temp = abs(int(n) - num)
        if temp < min:
            min = temp
            str = str(num)
else:
    border2 = int("".join(border_b))
    list_num = [border2, int(str4)]
    min = int(n)
    for num in list_num:
        temp = abs(int(n) - num)
        if temp < min:
            min = temp
            str = str(num)
