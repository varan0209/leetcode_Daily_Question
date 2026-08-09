class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lo, hi = min(nums), max(nums)
        s = set(nums)
        return [x for x in range(lo, hi + 1) if x not in s]