class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        best_len = -1
        left = 0
        curr = 0
        for right in range(n):
            curr += nums[right]
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            if curr == target:
                best_len = max(best_len, right - left + 1)

        return n - best_len if best_len != -1 else -1