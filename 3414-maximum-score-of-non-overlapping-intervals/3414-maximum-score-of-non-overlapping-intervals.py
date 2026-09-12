from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])  # indices sorted by r asc
        r_sorted = [intervals[i][1] for i in order]

        # dp[i][k] = (weight, sorted_index_tuple) best using at most k intervals
        # chosen among the first i intervals in sorted (by r) order.
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(1, n + 1):
            idx = order[i - 1]
            l, r, w = intervals[idx]
            p = bisect_left(r_sorted, l, 0, i - 1)  # count of r < l among first i-1
            row = dp[i]
            prev_row = dp[i - 1]
            src_row = dp[p]
            for k in range(5):
                best = prev_row[k]  # skip current interval
                if k >= 1:
                    prevW, prevTuple = src_row[k - 1]
                    takeW = prevW + w
                    takeTuple = tuple(sorted(prevTuple + (idx,)))
                    if takeW > best[0] or (takeW == best[0] and takeTuple < best[1]):
                        best = (takeW, takeTuple)
                row[k] = best

        best = dp[n][0]
        for k in range(1, 5):
            cand = dp[n][k]
            if cand[0] > best[0] or (cand[0] == best[0] and cand[1] < best[1]):
                best = cand

        return list(best[1])