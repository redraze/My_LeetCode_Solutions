# doubly linked list nodes
class Node:
    def __init__(self, key=None, value=None, prevNode=None, nextNode=None):
        self.key = key
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode


class LRUCache:
    def __init__(self, capacity: int):
        self.hashMap = {}
        self.used = 0
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.tail.nextNode = self.head
        self.head.prevNode = self.tail

    def get(self, key: int) -> int:
        # node is not in list
        if (key not in self.hashMap):
            return -1

        # move node to front of list
        if (self.head.prevNode.key != key):
            self.makeMRU(key)

        return self.hashMap[key].value

    def put(self, key: int, value: int) -> None:
        # check if key is already employed
        if (key in self.hashMap):
            self.hashMap[key].value = value
            self.makeMRU(key)
            return

        # delete LRU node
        if (self.used == self.cap):
            LRUNode = self.tail.nextNode
            newLRUNode = LRUNode.nextNode

            self.tail.nextNode = newLRUNode
            newLRUNode.prevNode = self.tail

            del self.hashMap[LRUNode.key]
            self.used -= 1
        
        # insert new node at front of list
        newNode = Node(key, value)

        prev = self.head.prevNode

        self.head.prevNode = newNode
        prev.nextNode = newNode

        newNode.nextNode = self.head
        newNode.prevNode = prev

        self.hashMap[key] = newNode
        self.used += 1

    def makeMRU(self, key) -> None:
        newMRU = self.hashMap[key]

        # remove references from surrounding nodes
        newMRU.prevNode.nextNode = newMRU.nextNode
        newMRU.nextNode.prevNode = newMRU.prevNode

        # re-insert node at front of list
        prevMRU = self.head.prevNode

        prevMRU.nextNode = newMRU
        self.head.prevNode = newMRU

        newMRU.nextNode = self.head
        newMRU.prevNode = prevMRU

        return
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
