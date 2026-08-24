class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Build prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # Alice can take all stones
        ans = stones[-1]

        # Try every possible prefix from right to left
        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans