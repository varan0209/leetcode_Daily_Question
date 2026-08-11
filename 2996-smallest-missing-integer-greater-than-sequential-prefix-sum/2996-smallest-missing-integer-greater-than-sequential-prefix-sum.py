class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1
        total = sum(nums[:i])
        
        s = set(nums)
        while total in s:
            total += 1
        return total