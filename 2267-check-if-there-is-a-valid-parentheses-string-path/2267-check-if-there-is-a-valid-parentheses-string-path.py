class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        
        # Optimization 1: A valid path must have an even length.
        # Total steps in any down-right path is m + n - 1.
        if (m + n - 1) % 2 != 0:
            return False
            
        # Optimization 2: Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        # Memoization set to track visited states: (row, col, balance)
        memo = set()
        
        def dfs(r, c, balance):
            # Update balance based on the current cell's character
            balance += 1 if grid[r][c] == '(' else -1
            
            # If balance drops below 0, this path is invalid
            if balance < 0:
                return False
                
            # If we reach the destination, verify if all brackets are perfectly matched
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            state = (r, c, balance)
            if state in memo:
                return False
            memo.add(state)
            
            # Move Down
            if r + 1 < m:
                if dfs(r + 1, c, balance):
                    return True
                    
            # Move Right
            if c + 1 < n:
                if dfs(r, c + 1, balance):
                    return True
                    
            return False

        return dfs(0, 0, 0)