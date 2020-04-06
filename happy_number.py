class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)

            som = 0
            while n:
                som += (n % 10) ** 2
                n //= 10
            n = som

        return n == 1
 
