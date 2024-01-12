from DoublyLinkList import *
from collections import OrderedDict

class LRU:
    def __init__(self, elements) -> None:
        self.dll = doublyLinkList()
        self.dic = OrderedDict()
        self.track = -1
        self.length = elements

    def put(self, key,  data):
        assert self.track <= self.length
        if key in self.dic:
            object = self.dic.pop(key)
            self.dll.remove(object)
            self.track -= 1
        n = self.dll.insert(data)
        self.track += 1
        self.dic[key] = n
        if self.track == self.length:
            oldest_key, oldest_node = self.dic.popitem(last=False)
            self.dll.remove(oldest_node)
            self.track -= 1
    
    def get(self, key):
        if key in self.dic:
            node = self.dic.pop(key)
            self.dic[key] = node
            self.dll.remove(node)
            self.dll.insert(node.data)
            return node.data
        else:
            return -1
            

    def tra(self):
        print("Least Recently Used")
        for key, value in self.dic.items():
            print([key, value.data])
        print("Recently Used")

    

# l = LRU(2)

# print(l.put(1,1))
# print(l.put(2,2))
# print(l.get(1))
# print(l.put(3,3))
# print(l.get(2))
# #print(l.get(4))
# print(l.put(4,4))
# print(l.get(1))
# print(l.get(3))
# print(l.get(4))
# l.tra()