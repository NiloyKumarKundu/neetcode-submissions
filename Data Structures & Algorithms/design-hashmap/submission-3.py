class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode(-1, -1) for i in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        idx = key % 10000
        curNode = self.arr[idx]

        while curNode.next:
            if curNode.next.key == key:
                curNode.next.value = value
                return
            curNode = curNode.next
        curNode.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        idx = key % 10000
        curNode = self.arr[idx]

        while curNode.next:
            if curNode.next.key == key:
                return curNode.next.value
            curNode = curNode.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % 10000
        curNode = self.arr[idx]

        while curNode.next:
            if curNode.next.key == key:
                curNode.next.value = -1
                return
            curNode = curNode.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)