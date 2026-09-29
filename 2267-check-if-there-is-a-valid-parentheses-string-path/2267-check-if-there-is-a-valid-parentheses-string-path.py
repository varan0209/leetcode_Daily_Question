class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Optimization: The path length is always m + n - 1. 
        # A valid parentheses string must have an even length.
        if (m + n - 1) % 2 != 0:
            return False
            
        # Optimization: A valid path must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        memo = {}
        
        def dfs(r, c, bal):
            # Account for the current cell's parenthesis
            if grid[r][c] == '(':
                bal += 1
            else:
                bal -= 1
                
            # If closed parentheses exceed open ones, it's invalid
            if bal < 0:
                return False
                
            # Pruning: If the remaining steps are fewer than the open balance, 
            # we can never balance it back to 0.
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if bal > remaining_steps:
                return False
                
            # Base Case: Reached the bottom-right corner
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            state = (r, c, bal)
            if state in memo:
                return memo[state]
                
            # Explore moving down and moving right
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, bal)
            if c + 1 < n:
                res = res or dfs(r, c + 1, bal)
                
            memo[state] = res
            return res
            
        return dfs(0, 0, 0)