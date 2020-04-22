# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows, cols = binaryMatrix.dimensions()
        current_row = 0
        current_col = cols -1
        while current_row < rows and current_col >=0:
            if binaryMatrix.get(current_row, current_col)==0:
                current_row +=1
            else:
                current_col -=1
        if current_col!=cols-1:
            return current_col+1
        else:
            return -1
