class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_pal = [bytearray(n) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            is_pal[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = 1

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= k:
                start = i - k
                if is_pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)
            if i >= k + 1:
                start = i - (k + 1)
                if is_pal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)
        return dp[n]