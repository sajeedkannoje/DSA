class  DoublyLinkedList:
    def __init__(self, key : int, val: int ):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # define a hash map for easy access
        self.hashMap = {}
        self.head = DoublyLinkedList(-1, -1)
        self.tail = DoublyLinkedList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        self.remove_node(self.hashMap[key])
        self.add_node_to_tail(self.hashMap[key])
        return self.hashMap[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove_node(self.hashMap[key])
        node = DoublyLinkedList(key, value)
        self.hashMap[key] = node
        
        if len(self.hashMap) > self.capacity:
            del self.hashMap[self.head.next.key]
            self.remove_node(self.head.next)

        self.add_node_to_tail(node)


    def remove_node(self, node: DoublyLinkedList) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node_to_tail(self, node: DoublyLinkedList) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next =  node
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)