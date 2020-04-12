class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) ==0:
            return 0
        if len(stones) == 1:
            return 1
        while len(stones)>1:
            stones.sort()
            max1,max2=stones[-1],stones[-2]
            if max1==max2:
                stones.pop(-1)
                stones.pop(-1)
            else:
                max1 = abs(max1-max2)
                stones.pop(-1)
                stones[-1] = max1
        if len(stones):
            return stones[-1]
        return 0
