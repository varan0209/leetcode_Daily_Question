class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        
        lo, hi = min(i, j), max(i, j)
        
        # Option 1: remove both from the front
        opt1 = hi + 1
        # Option 2: remove both from the back
        opt2 = n - lo
        # Option 3: remove one from the front, the other from the back
        opt3 = (lo + 1) + (n - hi)
        
        return min(opt1, opt2, opt3)