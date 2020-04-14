class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        m_left = 0
        l_string = len(s)
        for direction, amount in shift:
            if direction == 0:
                m_left += amount
            else:
                m_left -=amount
        m_left = m_left % l_string
        return s[m_left:] + s[:m_left]
