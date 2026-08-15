class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for x in nums:
            total ^= x
        
        if total != 0:
            return n
        
        if any(x != 0 for x in nums):
            return n - 1
        else:
            return 0