
class ListNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class doublyLinkList:

    def __init__(self) -> None:
        self.HEAD = ListNode("Least Recently Used")
        self.TAIL = ListNode("Recently Used")
        self.Formation()
    def Formation(self):
        self.HEAD.next = self.TAIL
        self.TAIL.prev = self.HEAD
    
    def insert(self, data):
        newNode = ListNode(data)
        temp = self.TAIL.prev
        temp.next = newNode
        self.TAIL.prev = newNode
        newNode.prev = temp
        newNode.next = self.TAIL
        return newNode
    
    def remove(self, node):
        tempP = node.prev
        tempN = node.next
        tempP.next = tempN
        tempN.prev = tempP

    def traverse(self):
        a = self.HEAD
        while a is not None:
            print(a.data)
            a = a.next

    def __len__(self):
        count = 0
        a = self
        while a is not None:
            a = a.next
            count += 1
        return count
    




