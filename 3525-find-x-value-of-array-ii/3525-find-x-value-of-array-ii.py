class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        cur = nums[:]

        tree_P = [0] * (4 * n)
        tree_cnt = [None] * (4 * n)

        def leaf_value(val):
            r = val % k
            cnt1 = [0] * k
            cnt1[r] = 1
            return r, cnt1

        def combine(left, right):
            if left is None:
                return right
            if right is None:
                return left
            PL, cnt1L = left
            PR, cnt1R = right
            shifted = [0] * k
            for t in range(k):
                c = cnt1R[t]
                if c:
                    shifted[(PL * t) % k] += c
            combined_cnt1 = [cnt1L[b] + shifted[b] for b in range(k)]
            combined_P = (PL * PR) % k
            return combined_P, combined_cnt1

        def build(node, l, r):
            if l == r:
                P, cnt1 = leaf_value(cur[l])
                tree_P[node] = P
                tree_cnt[node] = cnt1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node)

        def pull(node):
            left = (tree_P[2 * node], tree_cnt[2 * node])
            right = (tree_P[2 * node + 1], tree_cnt[2 * node + 1])
            P, cnt1 = combine(left, right)
            tree_P[node] = P
            tree_cnt[node] = cnt1

        def update(node, l, r, idx):
            if l == r:
                P, cnt1 = leaf_value(cur[idx])
                tree_P[node] = P
                tree_cnt[node] = cnt1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx)
            else:
                update(2 * node + 1, mid + 1, r, idx)
            pull(node)

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return None
            if ql <= l and r <= qr:
                return (tree_P[node], tree_cnt[node])
            mid = (l + r) // 2
            left = query(2 * node, l, mid, ql, qr)
            right = query(2 * node + 1, mid + 1, r, ql, qr)
            return combine(left, right)

        build(1, 0, n - 1)

        result = []
        for idx, val, start, x in queries:
            cur[idx] = val
            update(1, 0, n - 1, idx)
            P, cnt1 = query(1, 0, n - 1, start, n - 1)
            result.append(cnt1[x])

        return result