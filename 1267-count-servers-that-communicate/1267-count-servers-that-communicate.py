class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row = [sum(r) for r in grid]
        col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    count += 1
        return count  