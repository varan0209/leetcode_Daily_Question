class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        n = len(coins)
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        # Precompute LCM for all non-empty subsets
        subset_lcm = [0] * (1 << n)
        for mask in range(1, 1 << n):
            # find lowest set bit
            low_bit = mask & (-mask)
            idx = low_bit.bit_length() - 1
            prev = mask ^ low_bit
            if prev == 0:
                subset_lcm[mask] = coins[idx]
            else:
                subset_lcm[mask] = lcm(subset_lcm[prev], coins[idx])
        
        def count_le(amount):
            total = 0
            for mask in range(1, 1 << n):
                bits = bin(mask).count('1')
                l = subset_lcm[mask]
                cnt = amount // l
                if bits % 2 == 1:
                    total += cnt
                else:
                    total -= cnt
            return total
        
        lo, hi = 1, min(coins) * k
        
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        
        return lo