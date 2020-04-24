class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.first_key = None
        self.last_key = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        value = self.cache[key]['value']
        if key != self.last_key:
            self.remove_key(key)
            self.insert_key(key, value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove_key(key)
        elif len(self.cache) == self.capacity:
            self.remove_key(self.first_key)
            
        self.insert_key(key, value)
    
    def insert_key(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.cache[key] = {'value': value, 'prev_key': None, 'next_key': None}
        if len(self.cache) == 1:
            self.first_key = key
        else:
            self.cache[key]['prev_key'] = self.last_key
            self.cache[self.last_key]['next_key'] = key
        self.last_key = key
        
    def remove_key(self, key):
        """
        :type key: int
        :rtype: None
        """
        prev_key = self.cache[key]['prev_key']
        next_key = self.cache[key]['next_key']
        
        if key == self.first_key:
            self.first_key = next_key
        else:
            self.cache[prev_key]['next_key'] = next_key
            
        if key == self.last_key:
            self.last_key = prev_key
        else:
            self.cache[next_key]['prev_key'] = prev_key 
            
        del self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
