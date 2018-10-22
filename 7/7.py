class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_list = []
        if x < 0:
            Zhengshu = False
            x = -x
        else:
            Zhengshu = True

        while x:
            num_list.append(x % 10)
            x = x / 10

        num = 0
        for i in num_list:
            num = i + 10 * num

        if num > 2 ** 31 - 1:
            return 0

        if Zhengshu:
            return num
        else:
            return -num
