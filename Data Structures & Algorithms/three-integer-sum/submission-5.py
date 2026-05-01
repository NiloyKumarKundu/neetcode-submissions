class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        # print(nums)
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while (l < r):
                # print(f"i: {nums[i]}, l: {nums[l]}, r: {nums[r]}")
                if nums[l] + nums[r] == -nums[i]:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
                
            
        return [list(t) for t in res]