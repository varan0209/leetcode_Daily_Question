class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
        current_max = -float('inf')
        for i in range(n):
            current_max = max(current_max, nums[i])
            if current_max - suff_min[i] <= k:
                return i
        return -1