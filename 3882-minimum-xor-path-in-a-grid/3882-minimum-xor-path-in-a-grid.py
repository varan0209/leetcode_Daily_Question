class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # reach[j] = set of XOR values achievable at cell (current row, j)
        reach = [None] * n
        for i in range(m):
            for j in range(n):
                g = grid[i][j]
                if i == 0 and j == 0:
                    reach[0] = {g}
                    continue
                prev = set()
                if i > 0:
                    prev |= reach[j]          # from above (previous row's value)
                if j > 0:
                    prev |= reach[j - 1]      # from the left (already updated this row)
                reach[j] = {v ^ g for v in prev}
        return min(reach[n - 1])