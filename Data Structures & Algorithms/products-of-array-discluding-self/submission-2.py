class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        mul = nums[0]
        for i in range(1, len(nums)):
            pre[i] = mul
            mul *= nums[i]
        
        mul = nums[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            post[i] = mul
            mul *= nums[i]

        post[0] = mul

        res = [i * j for i, j in zip(pre, post)]
            

        return res
            



        
        