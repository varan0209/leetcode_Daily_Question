class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        vals = sorted(nums1)
        n = len(vals)
        T = vals[0] % 2          # forced target parity = parity of the minimum
        seen_odd = (T == 1)      # has an earlier (smaller) odd element appeared?

        for k in range(1, n):
            q = vals[k] % 2
            if q != T and not seen_odd:
                return False
            if q == 1:
                seen_odd = True

        return True