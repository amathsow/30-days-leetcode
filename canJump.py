class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)-1
        for i in range(n-1,-1,-1):
            if nums[i] + i>=n:
                n = i
        return n ==0
