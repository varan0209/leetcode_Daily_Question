class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        max_bal = m + n
        dp = [[None] * n for _ in range(m)]

        def delta(i, j):
            return 1 if grid[i][j] == '(' else -1

        dp[0][0] = [False] * (max_bal + 1)
        dp[0][0][1] = True  # already know grid[0][0] == '('

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cur = [False] * (max_bal + 1)
                d = delta(i, j)
                sources = []
                if i > 0 and dp[i-1][j] is not None:
                    sources.append(dp[i-1][j])
                if j > 0 and dp[i][j-1] is not None:
                    sources.append(dp[i][j-1])
                any_set = False
                for src in sources:
                    for b in range(max_bal + 1):
                        if src[b]:
                            nb = b + d
                            if 0 <= nb <= max_bal:
                                cur[nb] = True
                                any_set = True
                dp[i][j] = cur if any_set else None

        if dp[m-1][n-1] is None:
            return False
        return dp[m-1][n-1][0]