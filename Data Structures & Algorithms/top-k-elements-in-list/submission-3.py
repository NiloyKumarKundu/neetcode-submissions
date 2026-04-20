class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        flag = defaultdict(int)

        for i in nums:
            flag[i] += 1
        
        sorted_res = sorted(flag.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_res[i][0])
        return res