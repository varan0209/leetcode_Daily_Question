import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')
        K1 = k + 1
        dist = [INF] * (n * K1)      # dist[v*K1 + r]: best cost at v with current run length r
        min_r = [K1] * n             # smallest run length already finalized at v (dominates larger r)
        dist[0 * K1 + 1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, v, r = heapq.heappop(heap)
            if d > dist[v * K1 + r] or r >= min_r[v]:
                continue
            min_r[v] = r
            if v == n - 1:
                return d            # first pop of target is optimal (Dijkstra order)
            lv = labels[v]
            for w, wt in adj[v]:
                nr = r + 1 if labels[w] == lv else 1
                if nr > k or nr >= min_r[w]:
                    continue
                nd = d + wt
                idx = w * K1 + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(heap, (nd, w, nr))
        return -1