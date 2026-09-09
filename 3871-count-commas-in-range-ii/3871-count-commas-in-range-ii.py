class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        d = 1
        while 10 ** (d - 1) <= n:
            lo = 10 ** (d - 1)
            hi = min(n, 10 ** d - 1)
            count = hi - lo + 1
            total += count * ((d - 1) // 3)
            d += 1
        return total