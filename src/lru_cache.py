from collections import deque

class LRUCache(object):

    def __init__(self, capacity):
        self.max_size = capacity
        self.keys = deque()
        self.data = {}

    def get(self, key):
        if key in self.data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.data[key]
        else: return -1

    def put(self, key, value):
        if key in self.keys:
            self.data[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        elif len(self.data) < self.max_size:
            self.keys.append(key)
            self.data[key] = value
        elif self.max_size == len(self.data):
            x = self.keys.popleft()
            del self.data[x]
            self.keys.append(key)
            self.data[key] = value
