class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.deque = collections.deque()
        self.luckup = {}
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if len(self.deque)== 0:
            return -1
        
        while len(self.deque)>0 and self.deque[0] in self.luckup and self.luckup[self.deque[0]]>=2:
            self.deque.popleft()
        
        if len(self.deque)==0:
            return -1
        return self.deque[0]
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.luckup:
            self.luckup[value] +=1
        
        else:
            self.luckup[value] =1
            
        self.deque.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
