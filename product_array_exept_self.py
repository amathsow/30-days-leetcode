class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, cumulateMult=[], 1
        for x in nums:
            res.append(cumulateMult)
            cumulateMult*=x
        cumulateMult=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=cumulateMult
            cumulateMult*=nums[i]
        return res
