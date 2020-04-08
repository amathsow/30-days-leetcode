class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic = set(arr)
        cpt=0
        for elt in arr:
            if elt+1 in dic:
                cpt+=1
        return cpt
