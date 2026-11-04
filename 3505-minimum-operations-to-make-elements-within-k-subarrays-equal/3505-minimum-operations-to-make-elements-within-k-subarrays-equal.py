class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        LOG = 1 << m.bit_length()

        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(i, dc, ds):
            while i <= m:
                cnt[i] += dc
                sm[i] += ds
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        def kth(kk):  # smallest rank whose prefix count >= kk
            pos = 0
            step = LOG
            while step:
                nxt = pos + step
                if nxt <= m and cnt[nxt] < kk:
                    pos = nxt
                    kk -= cnt[nxt]
                step >>= 1
            return pos + 1

        # cost[i] = min ops to make nums[i..i+x-1] all equal (sum of |a - median|)
        w = n - x + 1
        cost = [0] * w
        total = 0
        mid = (x + 1) // 2
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                idx = kth(mid)
                med = vals[idx - 1]
                c_le, s_le = prefix(idx)
                cost[i - x + 1] = med * c_le - s_le + (total - s_le) - med * (x - c_le)

        INF = float('inf')
        prev = [0] * (n + 1)              # j = 0 windows: cost 0
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                best = cur[i - 1]
                cand = prev[i - x] + cost[i - x]
                cur[i] = cand if cand < best else best
            prev = cur
        return prev[n]