class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # rl[i][j]: resting cell index if the robot enters (i,j) moving right  (-1 = out of bounds)
        # dl[i][j]: resting cell index if the robot enters (i,j) moving down
        rl = [[-1] * (n + 1) for _ in range(m + 1)]
        dl = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    rl[i][j] = dl[i][j] = i * n + j
                else:
                    rl[i][j] = dl[i + 1][j]   # right into mirror -> turned down, enters (i+1, j) moving down
                    dl[i][j] = rl[i][j + 1]   # down into mirror -> turned right, enters (i, j+1) moving right

        dp = [0] * (m * n)
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                w = dp[i * n + j]
                if w == 0 or grid[i][j] == 1:
                    continue
                if j + 1 < n:
                    t = rl[i][j + 1]
                    if t >= 0:
                        dp[t] = (dp[t] + w) % MOD
                if i + 1 < m:
                    t = dl[i + 1][j]
                    if t >= 0:
                        dp[t] = (dp[t] + w) % MOD
        return dp[m * n - 1] % MOD