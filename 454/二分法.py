# -*- coding: utf-8 -*-
'''
所以可以采用二分的思路：
把四个区间分成两组：A、B一组，C、D一组，先从A、B组枚举出从两组中各取一个整数相加所有可能的结果，
将这些和排序（将这个排好序的vector记为ab），再枚举出C、D一组的所有情况，每算出一个c+d，就在ab中寻找是否存在c+d的相反数，
由于ab是已排序的，所以可以采用二分搜索的方式。考虑到ab可能存在重复的和，所以利用标准库的upper_bound 和lower_bound来求出重复的数有多少个
---------------------
作者：MonoTali
来源：CSDN
原文：https://blog.csdn.net/MonoTali/article/details/61627894
版权声明：本文为博主原创文章，转载请附上博文链接！
'''


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        HashMap = {}
        count = 0

        for i in range(len(A)):
            for j in range(len(B)):
                temp = A[i] + B[j]
                if HashMap.has_key(temp):
                    HashMap[temp] = HashMap[temp] + 1
                else:
                    HashMap[temp] = 1

        for i in range(len(C)):
            for j in range(len(D)):
                temp = -(C[i] + D[j])
                if HashMap.has_key(temp):
                    count = count + HashMap[temp]

        return count