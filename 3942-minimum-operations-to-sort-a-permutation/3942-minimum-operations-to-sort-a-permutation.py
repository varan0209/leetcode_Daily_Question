
class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        zero_idx = nums.index(0)

        ans = float('inf')

        # Case 1: Sort using rotations only
        if all(nums[(zero_idx + j) % n] == j for j in range(n)):
            ans = min(ans, zero_idx, n - zero_idx + 2)

        # Case 2: Sort using reversal and rotations
        rev = nums[::-1]
        rev_zero_idx = n - 1 - zero_idx

        if all(rev[(rev_zero_idx + j) % n] == j for j in range(n)):
            ans = min(
                ans,
                rev_zero_idx + 1,
                n - rev_zero_idx + 1
            )

        return ans if ans != float('inf') else -1
