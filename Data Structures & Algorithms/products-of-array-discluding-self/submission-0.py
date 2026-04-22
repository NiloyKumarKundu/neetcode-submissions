class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            mul = 1
            for j in range(0, len(nums)):
                if i != j:
                    mul *= nums[j]
            res.append(mul)
        return res
        