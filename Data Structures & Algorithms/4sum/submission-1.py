class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        # print(nums)
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                # print(a, nums[j], nums[l], nums[r])
                # print(f"l: {nums[l]}, r: {nums[r]}")
                while l < r:
                    sum = a + nums[j] + nums[l] + nums[r]
                    # print(f"sum {sum}, nums[i]: {nums[i]} nums[j]: {nums[j]}, nums[l]: {nums[l]}, nums[r]: {nums[r]}")
                    if sum == target:
                        # print("Target matched")
                        res.append([a, nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1
        return res
        