class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            temp = b
            b = a
            a = temp
        a = list(a)
        b = list(b)
        len_a = len(a)
        len_b = len(b)
        res = []
        c = 0

        for i in range(len_b):
            a_num = int(a.pop())
            b_num = int(b.pop())

            temp = a_num + b_num + c
            if temp >= 2:
                c = 1
                res_num = temp - 2
            else:
                c = 0
                res_num = temp

            res = list([str(res_num)]) + res

        for i in range(len_b, len_a):
            a_num = int(a.pop())

            temp = a_num + c
            if temp >= 2:
                c = 1
                res_num = temp - 2
            else:
                c = 0
                res_num = temp
            res = list([str(res_num)]) + res
        if c == 1:
            res = list(['1']) + res
        string = ''.join(res)
        return string



a = '1010'
b = '1011'
res = Solution().addBinary(a, b)
