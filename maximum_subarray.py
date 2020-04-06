from sys import maxint 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_big = -maxint - 1
        max_last = 0
        size = len(nums)
        for i in range(0, size): 
            max_last = max_last + nums[i] 
            if (max_big < max_last): 
                max_big = max_last
                
            if max_last < 0: 
                max_last = 0   
        return max_big
        
