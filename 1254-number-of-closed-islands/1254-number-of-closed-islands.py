class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        g = [row[:] for row in grid]  # don't mutate the input

        def flood(sr, sc):
            stack = [(sr, sc)]
            g[sr][sc] = 1
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < m and 0 <= nc < n and g[nr][nc] == 0:
                        g[nr][nc] = 1
                        stack.append((nr, nc))

        # erase every island touching the border (they can't be closed)
        for r in range(m):
            for c in range(n):
                if (r in (0, m - 1) or c in (0, n - 1)) and g[r][c] == 0:
                    flood(r, c)

        # every remaining island is closed
        count = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if g[r][c] == 0:
                    count += 1
                    flood(r, c)
        return count