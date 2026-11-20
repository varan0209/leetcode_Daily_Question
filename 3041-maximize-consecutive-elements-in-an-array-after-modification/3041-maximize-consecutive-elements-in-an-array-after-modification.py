
class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()

        dp = {}
        ans = 0

        for x in nums:
            # Save previous DP values before using current element
            prev_x = dp.get(x, 0)
            prev_x_minus_1 = dp.get(x - 1, 0)

            # Option 1: Keep x unchanged
            dp[x] = max(dp.get(x, 0), prev_x_minus_1 + 1)

            # Option 2: Increase x to x + 1
            dp[x + 1] = max(dp.get(x + 1, 0), prev_x + 1)

            ans = max(ans, dp[x], dp[x + 1])

        return ans
