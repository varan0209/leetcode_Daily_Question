
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, left, right):
            if lazy[node] == 0:
                return

            d = lazy[node]
            length = right - left + 1

            tree_sq[node] = (
                tree_sq[node]
                + 2 * d * tree_sum[node]
                + d * d * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + d * length
            ) % MOD

            if left != right:
                lazy[node * 2] = (lazy[node * 2] + d) % MOD
                lazy[node * 2 + 1] = (
                    lazy[node * 2 + 1] + d
                ) % MOD

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            push(node, left, right)

            if qr < left or right < ql:
                return

            if ql <= left and right <= qr:
                d = 1
                length = right - left + 1

                tree_sq[node] = (
                    tree_sq[node]
                    + 2 * tree_sum[node]
                    + length
                ) % MOD

                tree_sum[node] = (
                    tree_sum[node] + length
                ) % MOD

                if left != right:
                    lazy[node * 2] += d
                    lazy[node * 2 + 1] += d

                return

            mid = (left + right) // 2

            update(node * 2, left, mid, ql, qr)
            update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + tree_sq[1]) % MOD
            last[x] = i

        return ans
