class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        
        for num in stones:
            heapq.heappush(max_heap, -num)

        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            print(f"x: {x}, y: {y}")

            if x == y:
                print(f"coninue: {x, y}")
                continue
            if x < y:
                
                heapq.heappush(max_heap, -(y - x))
                print(f"y - x: {y - x}, max_heap: {max_heap}")
        return -max_heap[0] if len(max_heap) > 0 else 0