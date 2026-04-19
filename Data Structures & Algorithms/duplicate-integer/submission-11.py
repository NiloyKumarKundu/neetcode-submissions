class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        a = nums.copy()
        if length == 0 or length == 1:
            return False

        a.sort()
        for i in range(length - 1):
            if (a[i] == a[i + 1]):
                return True
        return False
        