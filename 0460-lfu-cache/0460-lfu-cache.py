class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def addFront(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def removeNode(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def removeLast(self):

        if self.size == 0:
            return None

        node = self.tail.prev
        self.removeNode(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0
        self.minFreq = 0

        self.keyNode = {}
        self.freqList = {}

    def update(self, node):

        freq = node.freq

        self.freqList[freq].removeNode(node)

        if freq == self.minFreq and self.freqList[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        if node.freq not in self.freqList:
            self.freqList[node.freq] = DLL()

        self.freqList[node.freq].addFront(node)

    def get(self, key: int) -> int:

        if key not in self.keyNode:
            return -1

        node = self.keyNode[key]
        self.update(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.keyNode:

            node = self.keyNode[key]
            node.value = value
            self.update(node)
            return

        if self.size == self.capacity:

            lfu = self.freqList[self.minFreq].removeLast()
            del self.keyNode[lfu.key]
            self.size -= 1

        node = Node(key, value)

        self.minFreq = 1

        if 1 not in self.freqList:
            self.freqList[1] = DLL()

        self.freqList[1].addFront(node)

        self.keyNode[key] = node

        self.size += 1