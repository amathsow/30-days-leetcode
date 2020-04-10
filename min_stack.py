class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack= []
        self.minval = sys.maxint
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (x<=self.minval):
            self.stack.append(self.minval)
            self.minval=x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if(self.stack and self.stack.pop()==self.minval): 
            self.minval=self.stack.pop() 

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval
