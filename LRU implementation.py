#OrderedDict is a kind of dictionary which preserves the order in which elements are added to it. In normal dictionary when u print the elemnts the they are printed in a random order whereras in OrderedDict they are printed in the order they've been added to to the dict. All the operations in OrderedDict takes O(1) time. Internally it is implemented using a doubly linked list hence its space complexity is higher then normal dict.
from collections import OrderedDict
class LRUcache:
    def __init__(self,capacity):
        self.cache=OrderedDict()
        self.capacity=capacity
    def getelement(self,key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def addelement(self,key,value):
        self.cache[key]=value
        self.cache.move_to_end(key)
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)
cache=LRUcache(2)
cache.addelement(1, 1)
print(cache.cache)
cache.addelement(2, 2)
print(cache.cache)
cache.getelement(1)
print(cache.cache)
cache.addelement(3, 3)
print(cache.cache)
cache.getelement(2)
print(cache.cache)
cache.addelement(4, 4)
print(cache.cache)
cache.getelement(1)
print(cache.cache)
cache.getelement(3)
print(cache.cache)
cache.getelement(4)
print(cache.cache)
