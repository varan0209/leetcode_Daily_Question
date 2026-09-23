class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        target = sum(nums) - k
        n = len(nums)

        if target < 0:
            return -1

        if target == 0:
            return n

        max_len = 0
        total = 0
        i = 0

        for j in range(n):
            total += nums[j]

            while total > target and i <= j:
                total -= nums[i]
                i += 1

            if total == target:
                max_len = max(max_len, j - i + 1)

        return -1 if max_len == 0 else n - max_len