class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        # node = [size, lchar, rchar, prefix, suffix, best]
        tree = [None] * (4 * n)

        def merge(left, right):
            size = left[0] + right[0]
            lchar, rchar = left[1], right[2]
            prefix = left[3]
            if left[3] == left[0] and left[1] == right[1]:
                prefix += right[3]
            suffix = right[4]
            if right[4] == right[0] and right[2] == left[2]:
                suffix += left[4]
            best = max(left[5], right[5])
            if left[2] == right[1]:
                best = max(best, left[4] + right[3])
            return [size, lchar, rchar, prefix, suffix, best]

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = [1, c, c, 1, 1, 1]
                return
            mid = (l + r) // 2
            build(2*node, l, mid)
            build(2*node+1, mid+1, r)
            tree[node] = merge(tree[2*node], tree[2*node+1])

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = [1, ch, ch, 1, 1, 1]
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2*node, l, mid, idx, ch)
            else:
                update(2*node+1, mid+1, r, idx, ch)
            tree[node] = merge(tree[2*node], tree[2*node+1])

        build(1, 0, n - 1)

        result = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            result.append(tree[1][5])
        return result