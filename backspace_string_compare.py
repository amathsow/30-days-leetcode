class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def compare_diez(s):
            stack = []
            for i in s:
                if i != "#":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
            return "".join(stack)

        return compare_diez(S) == compare_diez(T)
