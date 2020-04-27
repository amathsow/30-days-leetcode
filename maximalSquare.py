class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        row = len(matrix)
        if row == 0:
            return res
        col = len(matrix[0])
        state = [[0 for y in range(col)] for z in range(row)]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    state[i][j] = 1
                    res = 1
                    
        for i in range(1, row):
            for j in range(1,col):
                if state[i][j] != 0:
                    state[i][j] = 1+ min(min(state[i-1][j],state[i-1][j-1]),state[i][j-1])
                    if res < state[i][j]:
                        res = state[i][j]
        return res*res
