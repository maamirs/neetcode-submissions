class Node:
    def __init__(self, key=0 , value=0):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()
        
        # head --- tail
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove (self, node):

        # head -- [] -- tail

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    

    def _insert_right(self, node):

        # head ---[] -- [] -- tail

        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node
        

    def get(self, key: int) -> int:

        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self._remove(node)
        self._insert_right(node)

        return node.value

        

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            self._remove(self.hashmap[key])
        
        newnode = Node(key,value)

        self.hashmap[key] = newnode

        self._insert_right(newnode)

        if len(self.hashmap) > self.capacity:
            lru = self.head.next
            # head -- [] --[] --tail

            self._remove(lru)
            del self.hashmap[lru.key]

        
