class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            best = INF
            for d in (1, 2, 3):
                if j - d >= 0:
                    cand = dp[j - d] + d * d
                    if cand < best:
                        best = cand
            dp[j] = costs[j - 1] + best     # costs is 1-indexed in the statement
        return dp[n]