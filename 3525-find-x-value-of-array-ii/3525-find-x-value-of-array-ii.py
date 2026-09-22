from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Pad n to the next power of 2 for a simplified iterative segment tree
        m = 1
        while m < n:
            m *= 2
            
        tree_prod = [1] * (2 * m)
        tree_counts = [[0] * k for _ in range(2 * m)]
        
        # Initialize the leaves of the segment tree
        for i in range(n):
            val = nums[i] % k
            tree_prod[m + i] = val
            tree_counts[m + i][val] = 1
            
        # Build the initial segment tree
        for i in range(m - 1, 0, -1):
            L = 2 * i
            R = 2 * i + 1
            L_prod = tree_prod[L]
            L_counts = tree_counts[L]
            R_prod = tree_prod[R]
            R_counts = tree_counts[R]
            
            tree_prod[i] = (L_prod * R_prod) % k
            for v in range(k):
                tree_counts[i][v] = L_counts[v]
            for v in range(k):
                if R_counts[v]:
                    nv = (L_prod * v) % k
                    tree_counts[i][nv] += R_counts[v]
                    
        ans = []
        for idx, value, start, x in queries:
            # 1. Point Update
            node = m + idx
            val = value % k
            tree_prod[node] = val
            for i in range(k):
                tree_counts[node][i] = 0
            tree_counts[node][val] = 1
            
            node //= 2
            while node > 0:
                L = 2 * node
                R = 2 * node + 1
                L_prod = tree_prod[L]
                L_counts = tree_counts[L]
                R_prod = tree_prod[R]
                R_counts = tree_counts[R]
                
                tree_prod[node] = (L_prod * R_prod) % k
                for v in range(k):
                    tree_counts[node][v] = L_counts[v]
                for v in range(k):
                    if R_counts[v]:
                        nv = (L_prod * v) % k
                        tree_counts[node][nv] += R_counts[v]
                node //= 2
                
            # 2. Range Query [start, n - 1]
            l = m + start
            r = m + n - 1
            
            left_nodes = []
            right_nodes = []
            
            # Find the nodes covering the query interval
            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2
                
            # Combine the nodes left-to-right
            curr_prod = 1
            curr_counts = [0] * k
            
            for node in left_nodes + right_nodes[::-1]:
                nxt_prod = (curr_prod * tree_prod[node]) % k
                nxt_counts = list(curr_counts)
                
                # Multiply combined past prefix products with current node's prefixes
                for v in range(k):
                    if tree_counts[node][v]:
                        nv = (curr_prod * v) % k
                        nxt_counts[nv] += tree_counts[node][v]
                        
                curr_prod = nxt_prod
                curr_counts = nxt_counts
                
            ans.append(curr_counts[x])
            
        return ans