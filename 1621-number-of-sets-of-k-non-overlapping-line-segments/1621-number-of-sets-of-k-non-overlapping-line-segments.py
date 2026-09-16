class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  # 0 segments: exactly one way (draw nothing)

        for j in range(1, k + 1):
            prefix = [0] * (n + 1)
            prefix[0] = dp[0][j - 1]
            for t in range(1, n + 1):
                prefix[t] = (prefix[t - 1] + dp[t][j - 1]) % MOD

            for i in range(1, n + 1):
                s = (prefix[i - 1] - dp[0][j - 1]) % MOD  # sum_{q=1}^{i-1} dp[q][j-1]
                dp[i][j] = (dp[i - 1][j] + s) % MOD

        return dp[n][k] % MOD