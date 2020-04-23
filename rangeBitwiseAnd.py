class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pos = 0
        while m != n:
            pos += 1
            m >>= 1
            n >>= 1

        return n << pos
