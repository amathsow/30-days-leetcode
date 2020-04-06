class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for st in strs:
            x = ' '.join(sorted(st))
            if x not in dic:
                dic[x]=[st]
            else:
                dic[x].append(st)
        return dic.values()
