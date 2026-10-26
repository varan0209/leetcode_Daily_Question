class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        count = 0

        for sr in range(m):
            for sc in range(n):
                if grid[sr][sc] > 0 and not seen[sr][sc]:
                    total = 0
                    seen[sr][sc] = True
                    stack = [(sr, sc)]
                    while stack:
                        r, c = stack.pop()
                        total += grid[r][c]
                        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not seen[nr][nc]:
                                seen[nr][nc] = True
                                stack.append((nr, nc))
                    if total % k == 0:
                        count += 1
        return count
        