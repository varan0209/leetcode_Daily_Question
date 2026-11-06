class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs = sorted(logs, key=lambda e: e[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        cnt = [0] * (n + 1)   # requests per server inside the current window
        active = 0            # servers with at least one request in the window
        ans = [0] * len(queries)
        l = r = 0
        m = len(logs)
        for qi in order:
            q = queries[qi]
            while r < m and logs[r][1] <= q:          # add requests up to time q
                s = logs[r][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                r += 1
            while l < r and logs[l][1] < q - x:       # drop requests before q - x
                s = logs[l][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                l += 1
            ans[qi] = n - active
        return ans