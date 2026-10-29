class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = [ord(c) - 97 for c in s]
        LOG = max(1, (n - 1).bit_length())
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        P0 = [0] * n                       # root-to-node parity mask (inclusive), initial string
        up = [[0] * n for _ in range(LOG)]  # up[k][v] = 2^k-th ancestor (root points to itself)

        # iterative DFS for Euler tour
        timer = 0
        P0[0] = 1 << chars[0]
        stack = [(0, -1, 0)]
        while stack:
            v, par, state = stack.pop()
            if state == 0:
                tin[v] = timer
                timer += 1
                up[0][v] = par if par >= 0 else v
                stack.append((v, par, 1))
                for w in adj[v]:
                    if w != par:
                        depth[w] = depth[v] + 1
                        P0[w] = P0[v] ^ (1 << chars[w])
                        stack.append((w, v, 0))
            else:
                tout[v] = timer - 1
        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        # Fenwick tree over XOR: range-xor update, point query
        bit = [0] * (n + 2)

        def bit_add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def bit_query(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def mask(x):
            return P0[x] ^ bit_query(tin[x])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), ord(parts[2]) - 97
                if chars[u] != c:
                    delta = (1 << chars[u]) ^ (1 << c)
                    chars[u] = c
                    bit_add(tin[u], delta)
                    bit_add(tout[u] + 1, delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                m = mask(u) ^ mask(v) ^ (1 << chars[l])
                ans.append(m & (m - 1) == 0)
        return ans