class ListNode:
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.num_buckets = 1000
        self.set = [ListNode(-1) for _ in range(self.num_buckets)]
        
    def __hash(self, key:int) -> int:
        return key % self.num_buckets
    def add(self, key: int) -> None:
        bucketIndex = self.__hash(key)
        curr = self.set[bucketIndex]

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        bucketIndex = self.__hash(key)
        curr = self.set[bucketIndex]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        
        bucketIndex = self.__hash(key)
        curr = self.set[bucketIndex]

        while curr:
            if curr.key == key:
                return True 
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)