class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        track,has=0,{0:-1}
        length=len(nums);
        ress_max=0;

        for i in range(0,length):
            track += (1 if nums[i]==1 else -1)
            if  track not in has:
                has[track]=i
            elif ress_max <i-has[track]:
                ress_max = i-has[track]
        return ress_max
