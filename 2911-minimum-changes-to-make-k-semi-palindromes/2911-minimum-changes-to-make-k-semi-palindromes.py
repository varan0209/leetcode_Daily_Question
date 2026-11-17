
class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # Precompute the cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Each group contains indices r, r+d, r+2d...
                    for r in range(d):
                        left = i + r
                        right = j - ((length - 1 - r) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for groups in range(1, k + 1):
            for i in range(2 * groups, n + 1):
                for t in range(2 * (groups - 1), i - 1):

                    dp[i][groups] = min(
                        dp[i][groups],
                        dp[t][groups - 1] + cost[t][i - 1]
                    )

        return dp[n][k]
