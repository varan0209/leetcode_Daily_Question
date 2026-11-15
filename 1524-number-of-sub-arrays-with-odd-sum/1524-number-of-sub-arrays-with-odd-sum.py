class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        even, odd = 1, 0      # counts of prefix sums (including the empty prefix) by parity
        parity = 0
        ans = 0
        for v in arr:
            parity ^= v & 1
            if parity:
                ans += even   # odd prefix minus an even prefix -> odd subarray sum
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % MOD