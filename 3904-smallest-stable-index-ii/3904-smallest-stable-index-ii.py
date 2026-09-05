class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prev = nums[-1]
        for i in range(n - 1, -1, -1):
            prev = min(nums[i], prev)
            suffix[i] = prev

        m = nums[0]
        for i in range(n):
            m = max(nums[i], m)
            if m - suffix[i] <= k:
                return i

        return -1