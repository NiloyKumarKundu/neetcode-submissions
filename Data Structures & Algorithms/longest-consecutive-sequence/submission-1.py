class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set()

        for num in nums:
            current = num
            store.add(current)
            while current + 1 in nums:
                store.add(current + 1)
                current += 1
            res = max(res, len(store))
            store.clear()
        return res

        



